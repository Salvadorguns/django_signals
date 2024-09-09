#Django Signals and Views Example
This project demonstrates the use of Django signals and custom views to create users, handle post_save signals, and work with a custom class (Rectangle) in a web application. It covers three signal handlers, a user creation form, and a simple view for rendering a rectangle's dimensions.

Table of Contents
Introduction
Features
Prerequisites
Installation
Usage
Views
Signals
Contributing
License
Introduction
This project focuses on using Django signals and views in a practical way. Key topics include:

Handling Django post_save signals for the User model.
Creating a custom view to add new users.
Implementing a view to display a simple geometric shape (Rectangle).
The signals demonstrate different approaches, including delayed execution, threading, and database transaction handling.

Features
User creation view with validation to prevent duplicate usernames.
Multiple post_save signal handlers for the User model.
Signal handlers demonstrate:
Long-running tasks with time.sleep().
Threaded execution of signal handlers.
Use of Django database transactions with signals.
Custom Rectangle class with a view to display its dimensions.
Prerequisites
Python 3.8+
Django 3.2+
Basic knowledge of Django signals and views.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/Salvadorguns/django_signals.git
Navigate to the project directory:

bash
Copy code
cd django_signals
Create a virtual environment:

bash
Copy code
python3 -m venv env
source env/bin/activate
Install the required packages:

bash
Copy code
pip install -r requirements.txt
Apply migrations and run the server:

bash
Copy code
python manage.py migrate
python manage.py runserver
Usage
Once the server is running, you can interact with the application through the following views:

1. User Creation View (/create_user/)
This view allows users to be created by submitting a form with a username and password. It checks for the existence of the user to avoid duplication:

URL: /create_user/
Method: POST
Fields:
username: The username for the new user.
password: The password for the new user.
Example response:

Success: "User {username} created successfully!"
Failure (user exists): "User {username} already exists!"
2. Rectangle View (/rectangle/)
This view creates a Rectangle object and displays its dimensions on the web page:

URL: /rectangle/
Context: Contains length and width of the rectangle.
3. Index View (/)
A simple index page rendered at the root URL:

URL: /
Views
1. create_user View
Handles user creation by checking for existing users and providing error handling for unique constraint violations.

python
Copy code
def create_user(request):
    # Create a new user with unique username and password
2. rectangle_view View
Displays the dimensions of a Rectangle object.

python
Copy code
def rectangle_view(request):
    # Render the rectangle's length and width
3. index View
Renders the homepage.

python
Copy code
def index(request):
    return render(request, 'index.html')
Signals
The post_save signal handlers for the User model demonstrate three different approaches:

1. user_saved_handler
This signal handler simulates a long-running task using time.sleep(5) and logs the user save action to a SignalLog model.

python
Copy code
@receiver(post_save, sender=User)
def user_saved_handler(sender, instance, **kwargs):
    time.sleep(5)  # Simulate a long-running task
2. user_saved_handler_thread
This handler prints the thread information and logs the user save event, demonstrating the use of threads with signal handling.

python
Copy code
@receiver(post_save, sender=User)
def user_saved_handler_thread(sender, instance, **kwargs):
    print(f"Signal handler thread: {threading.current_thread().name}")
3. user_saved_handler_transaction
This signal checks whether it is inside a database transaction block and logs the action accordingly.

python
Copy code
@receiver(post_save, sender=User)
def user_saved_handler_transaction(sender, instance, **kwargs):
    print(f"Inside transaction: {transaction.get_connection().in_atomic_block}")
Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for discussion.

License
This project is licensed under the MIT License. See the LICENSE file for more information.
