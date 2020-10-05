from django.shortcuts import render
from .cart import Cart
from .forms import CartAddBookForm
from shop.models import Book
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

@require_POST
def cart_add(request, book_id):
	cart = Cart(request)
	book = get_object_or_404(Book, id=book_id)
	form = CartAddBookForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(book=book,
				quantity=1,
				update_quantity=cd['update'])
	return redirect('cart:cart_detail')

def cart_remove(request, book_id):
	cart = Cart(request)
	book = get_object_or_404(Book, id=book_id)
	cart.remove(book)
	return redirect('cart:cart_detail')

def cart_detail(request):
	cart = Cart(request)
	return render(request, 'cart/detail.html', {'cart': cart})
