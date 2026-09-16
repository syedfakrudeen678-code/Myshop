from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order_id):
    """
    Task to send an email notification when an order is created.
    """

    order = Order.objects.get(id=order_id)
    subject = f'Order #{order_id} Confirmation'
    message =(
        
        f'Dear Customer,\n\nYour order #{order_id} has been successfully placed!'
    )
    
    mail_sent = send_mail(
        subject,
        message,
        'admin@myshop.com', [order.email]
    )
    return mail_sent