# Django Signals and Views Example
This project demonstrates the use of Django signals and custom views to create users, handle post_save signals, and work with a custom class (Rectangle) in a web application. It covers three signal handlers, a user creation form, and a simple view for rendering a rectangle's dimensions.

# Handling Django post_save signals for the User model.
# Creating a custom view to add new users.
# Implementing a view to display a simple geometric shape (Rectangle).
# The signals demonstrate different approaches, including delayed execution, threading, and database transaction handling.

# Features
1. User creation view with validation to prevent duplicate usernames.
2. Multiple post_save signal handlers for the User model.


# Use of Django database transactions with signals.
# Custom Rectangle class with a view to display its dimensions.


# Prerequisites
1. Python 3.8+
2. Django 3.2+
3. Basic knowledge of Django and Python.
4. Installation

# Clone the repository:

1. Copy code git clone https://github.com/Salvadorguns/django_signals.git

2. Navigate to the project directory:
    Copy code
    cd django_signals

3. Create a virtual environment:
    Copy code
    python3 -m venv env
    source env/bin/activate

4. Install the required packages:
    Copy code
    pip install -r requirements.txt

5.Apply migrations and run the server:
    Copy code
    python manage.py migrate
    python manage.py runserver


 

License
This project is licensed under the MIT License. See the LICENSE file for more information.
