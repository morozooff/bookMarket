from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from market.models import Book
from .basket import Basket
from .forms import BasketAddBookForm


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



