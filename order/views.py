from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from market.models import Book
from django.contrib.auth.models import User
from .models import Order, OrderItem
from .basket import Basket
from .forms import BasketAddBookForm, OrderCreateForm

from django.views.generic import DetailView, ListView


@require_POST
def basket_add(request, book_id):
    basket = Basket(request)
    book = get_object_or_404(Book, id = book_id)
    form = BasketAddBookForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        basket.add(book = book, quantity = cd['quantity'], update_quantity = cd['update'])

    return redirect('basket_detail')


def basket_remove(request, book_id):
    basket = Basket(request)
    book = get_object_or_404(Book, id = book_id)
    basket.remove(book)
    return redirect('basket_detail')


@login_required
def basket_detail(request):

    basket = Basket(request)
    return render(request, 'basket_detail.html', {'basket': basket})


def order_create(request):
    basket = Basket(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit = False)
            order.customer = request.user
            order.save()
            for item in basket:
                OrderItem.objects.create(order = order,
                                         book = item['book'],
                                         cost =item['cost'],
                                         quantity = item['quantity'])
            basket.clear()
            return render(request, 'created.html', {'order': order})

    else:
        form = OrderCreateForm
    return render(request, 'create.html', {'basket': basket, 'form': form})


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'


class UserOrderListView(ListView):
    model = Order
    template_name = 'my_orders.html'
    context_object_name = 'orders'
    ordering = ['-created']


    def get_queryset(self):
        user = get_object_or_404(User, id = self.request.user.id)
        return Order.objects.filter(customer = user)


