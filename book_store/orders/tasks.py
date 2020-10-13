from celery import shared_task
from .models import Order
from django.core.mail import send_mail

@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Your order {order_id}'
    message = f'Hello, you created order in our shop with id number {order_id}'

    mail_sent = send_mail(subject,
                        message,
                        'admin@book_store.com',
                        [order.email])

    return mail_sent
