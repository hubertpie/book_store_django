from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from orders.models import Order

@login_required
def profile(request):
	orders = Order.objects.filter(user=request.user)
	return render(request, 'account/profile.html', {'orders': orders})