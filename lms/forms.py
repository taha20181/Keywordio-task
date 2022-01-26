from django import forms
from .models import Book


class AddBookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['added_by', 'added_at']
