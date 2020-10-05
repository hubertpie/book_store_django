from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Book
from cart.forms import CartAddBookForm

def book_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	books = Book.objects.filter(available=True)
	cart_book_form = CartAddBookForm()
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		books = books.filter(category=category)
	return render(request, 
				'shop/book/list.html',
				{'books': books,
				'category': category,
				'categories': categories,
				'cart_book_form': cart_book_form})


def book_detail(request, id, slug):
	book = get_object_or_404(Book, id=id, slug=slug, available=True)
	book_category = get_object_or_404(Category, name=book.category)
	cart_book_form = CartAddBookForm()
	return render(request, 
				'shop/book/detail.html',
				{'book': book,
				'book_category': book_category,
				'cart_book_form': cart_book_form})