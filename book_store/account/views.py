from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from orders.models import Order
from .forms import AccountCreateForm
from django.contrib.auth import authenticate, login

@login_required
def profile(request):
	orders = Order.objects.filter(user=request.user)
	return render(request, 'account/profile.html', {'orders': orders})


def register(request):
	if request.method == 'POST':
		account_form = AccountCreateForm(request.POST)
		if account_form.is_valid():
			account_form.save()
			return redirect('shop:book_list')
	else:	
		account_form = AccountCreateForm()
	return render(request, 'account/register.html', {'account_form': account_form})
