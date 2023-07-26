from django import forms

from .models import Order

BOOK_QUANTITY_CHOICE = [(i, str(i)) for i in range(1, 16)]


class BasketAddBookForm(forms.Form):
    quantity = forms.TypedChoiceField(choices = BOOK_QUANTITY_CHOICE, coerce=int, label = "Количество")
    update = forms.BooleanField(required=False, initial=False, widget = forms.HiddenInput)


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'postal_code']
        labels = {'address': 'Введите свой адрес: ',
                  'postal_code': 'Введите почтовый индекс: '}


