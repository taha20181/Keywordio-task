from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import Book

@login_required(login_url='login_view')
def index(request):
    context = {
        'segment': 'index',
    }
    return render(request, 'index.html', context)


@login_required(login_url='login_view')
def add_book(request):
    data = request.POST
    
    if request.method == 'POST':
        book = Book()
        book.name = data['name']
        book.author = data['author']
        book.quantity = data['qty']
        book.added_by = request.user
        
        book.save()
        
        return redirect('show_books')

    return render(request, 'add_book.html')


@login_required(login_url='login_view')
def show_books(request):
    load_template = request.path.split('/')[1]
    books = Book.objects.all()
    
    context = {
        'books' : books,
        'segment' : load_template
    }
    
    return render(request, 'show_books.html', context)


@login_required(login_url='login_view')
def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    data = request.POST
    if request.method == 'POST':
        book.name = data['name']
        book.author = data['author']
        book.quantity = data['qty']
        
        book.save()
        return redirect('show_books')
        
    context = {
        'book' : book,
    }
    return render(request, 'update_book.html', context)


@login_required(login_url='login_view')
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    
    book.delete()
    
    return redirect('show_books')


def student_view(request):
    books = Book.objects.all()
    
    context = {
        'books' : books,
    }
    
    return render(request, 'student_view.html', context)