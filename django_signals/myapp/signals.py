from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SignalLog
import time
import threading
from django.db import transaction


#this one shows the synchronization of the signals
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    print(f"User {instance.username} has been saved!")
    start_time = time.time()
    time.sleep(5)  # Simulate a long-running task
    end_time = time.time()
    print(f"Signal handler completed in {end_time - start_time} seconds")
    SignalLog.objects.create(user=instance, action="User saved")


# this one shows the threading of the signals
@receiver(post_save, sender=User)
def user_saved_handler_thread(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")
    print(f"User {instance.username} has been saved! in threading")
    SignalLog.objects.create(user=instance, action="User saved in thread")

# this one shows the transaction on database
@receiver(post_save, sender=User)
def user_saved_handler_transaction(sender, instance, **kwargs):
    def on_commit_handler():
        print(f"User {instance.username} has been saved! in transaction")
        SignalLog.objects.create(user=instance, action="User saved in transaction")
    
    transaction.on_commit(on_commit_handler)