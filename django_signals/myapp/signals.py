from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time
import threading
from django.db import transaction



@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"User {instance.username} has been saved!")
    time.sleep(5)  # Simulate a long-running task
    print("Signal handler completed")

def user_saved_handler(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")
    print(f"User {instance.username} has been saved! for threading")

def user_saved_handler(sender, instance, **kwargs):
    print(f"User {instance.username} has been saved!")
    print(f"Inside transaction: {transaction.get_connection().in_atomic_block}")