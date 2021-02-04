from django import forms

from .models import Book 

class TestForm(forms.Form):
    text = forms.CharField(label='文字入力')
    num = forms.IntegerField(label='数量')

class BookAdd(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'publisher', 'page']