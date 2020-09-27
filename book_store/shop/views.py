from django.shortcuts import render
from .models import Category, Book

def book_list(request):
	books = Book.objects.all()
	return render(request, 'shop/book/list.html', {'books': books})