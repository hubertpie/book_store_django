from django.shortcuts import render
from .models import Category, Book

def book_list(request):
	return render(request, 'shop/book/list.html')