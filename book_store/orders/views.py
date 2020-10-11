from django.shortcuts import render, redirect
from django.urls import reverse
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        book=item['book'],
                                        price=item['price'],
                                        quantity=item['quantity'])

            cart.clear()
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
        
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'form':form, 'cart': cart})