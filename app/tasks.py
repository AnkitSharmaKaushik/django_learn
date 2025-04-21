from celery import shared_task
import time
from datetime import datetime

@shared_task
def slow_add(x, y):
    time.sleep(5)
    return x + y

@shared_task
def print_current_time():
    now = datetime.now()
    print(f"[CELERY TASK] Current Time: {now}")
    return now.isoformat()

#  Create an Async Task
# Let's say we want to simulate a time-consuming task like sending an email or processing data.

@shared_task
def process_user_data(user_id):
    print(f"Start processing user {user_id}")
    time.sleep(10)  # Simulate long process
    print(f"Finished processing user {user_id}")
    return f"Processed user {user_id}"


# Send WebSocket Notification from Celery
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def process_user_data(user_id):
    import time
    time.sleep(5)  # simulate delay
    message = f"User {user_id} processing complete!"

    # Send WebSocket message
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            "type": "send_notification",
            "message": message,
        },
    )
    return message


# Step-by-Step Email Notification Setup in Django
from django.core.mail import send_mail
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def process_user_data(user_id, email):
    import time
    time.sleep(5)  # simulate delay

    message = f"User {user_id} processing complete!"

    # ✅ WebSocket notification
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            "type": "send_notification",
            "message": message,
        },
    )

    # ✅ Email notification
    send_mail(
        subject="Your Process is Complete",
        message=f"Hello,\n\nYour task has been completed successfully.\n\nMessage: {message}",
        from_email=None,  # uses DEFAULT_FROM_EMAIL
        recipient_list=[email],
        fail_silently=False,
    )

    return message
