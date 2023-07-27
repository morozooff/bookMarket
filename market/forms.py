from django import forms

class SearchBookForm(forms.Form):
    search_request = forms.CharField(label = "Введите запрос по книгам:")
