from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.postgres.search import SearchVector
from .models import Category, Book
from cart.forms import CartAddBookForm
from .forms import SearchForm

def book_list(request, category_slug=None):
	search_form = SearchForm()
	query = None 
	category = None
	categories = Category.objects.all()
	books = Book.objects.filter(available=True)
	cart_book_form = CartAddBookForm()
	if 'query' in request.GET:
		form = SearchForm(request.GET)
		if form.is_valid():
			query = form.cleaned_data['query']
			books = Book.objects.annotate(search=SearchVector('title', 'author' ),).filter(search=query)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		books = books.filter(category=category)
	return render(request, 
				'shop/book/list.html',
				{'books': books,
				'category': category,
				'categories': categories,
				'cart_book_form': cart_book_form,
				'search_form': search_form,
				'query': query})


def book_detail(request, id, slug):
	book = get_object_or_404(Book, id=id, slug=slug, available=True)
	book_category = get_object_or_404(Category, name=book.category)
	cart_book_form = CartAddBookForm()
	return render(request, 
				'shop/book/detail.html',
				{'book': book,
				'book_category': book_category,
				'cart_book_form': cart_book_form})