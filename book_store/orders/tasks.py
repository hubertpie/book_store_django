
from django.core.mail import send_mail
from .models import Order


def order_created(order_id):
    """
    Task sending e-mail message after 
    placing order in shop
    """
    order = Order.objects.all(id=order_id)
    subject = f'Order #{order.id}'
    message = 'Hello {order.first_name}, you placed order in our shop. ID of your order is {order.id}'

    mail_sent = send_mail(subject,
                        message,
                        'admin@myshop.com',
                        [order.email])

    return mail_sent