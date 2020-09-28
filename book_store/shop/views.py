from django.shortcuts import render, get_object_or_404
from .models import Category, Book

def book_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	books = Book.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		books = Book.objects.filter(category=category, available=True)
	return render(request, 
				'shop/book/list.html',
				{'books': books,
				'category': category,
				'categories': categories})