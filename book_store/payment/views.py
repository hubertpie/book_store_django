import braintree
from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from django.contrib.auth import authenticate

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        # getting nonce token
        nonce = request.POST.get('payment_method_nonce', None)
        result = braintree.Transaction.sale({
            'amount': order.get_total_cost(),
            'payment_method_nonce': nonce,
            'options': {
            'submit_for_settlement': True
            }
        })

        if result.is_success:
            if request.user.is_authenticated:
                order.user = request.user
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')

    else:
        client_token = braintree.ClientToken.generate()
        return render(request,
                    'payment/process.html',
                    {'order': order,
                    'client_token': client_token})


def payment_done(request):
    return render(request, 'payment/done.html')

def payment_canceled(request):
    return render(request, 'payment/canceled.html')