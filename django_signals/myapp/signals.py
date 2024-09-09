# myapp/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import SignalLog
import time
import threading
from django.db import transaction

@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"User {instance.username} has been saved!")
    time.sleep(5)  # Simulate a long-running task
    print("Signal handler completed")
    SignalLog.objects.create(user=instance, action="User saved")

@receiver(post_save, sender=User)
def user_saved_handler_thread(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")
    print(f"User {instance.username} has been saved! for threading")
    SignalLog.objects.create(user=instance, action="User saved in thread")

@receiver(post_save, sender=User)
def user_saved_handler_transaction(sender, instance, **kwargs):
    print(f"User {instance.username} has been saved!")
    print(f"Inside transaction: {transaction.get_connection().in_atomic_block}")
    SignalLog.objects.create(user=instance, action="User saved in transaction")