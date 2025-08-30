Django OTP Registration with Twilio

A simple Django project that sends OTPs via Twilio SMS for user registration and verification.

Features

User registration with phone number

OTP sent via Twilio SMS

OTP verification for login/registration

Secure Twilio credentials using .env

Requirements

Python 3.10+

Django 4.x

Twilio account (trial or paid)

python-dotenv

twilio Python SDK

Installation

Clone the repository:

git clone https://github.com/amarraw/django-twilio-otp.git
cd django-twilio-otp


Create and activate virtual environment:

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Install dependencies:

pip install -r requirements.txt


Create .env file in the project root:

SECRET_KEY=your_django_secret_key
DEBUG=True
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_PHONE_NUMBER=+1XXXXXXXXXX


Apply migrations:

python manage.py makemigrations
python manage.py migrate


Run the server:

python manage.py runserver

Usage

Visit http://127.0.0.1:8000/users/register/

Enter your phone number (verified in Twilio trial account)

Receive OTP via SMS

Verify OTP to complete registration

Notes

Twilio trial account can only send SMS to verified numbers.

For production, upgrade Twilio to send SMS worldwide.

Keep .env secure, do not push to GitHub.

Dependencies

Django

Twilio (pip install twilio)

Python-dotenv (pip install python-dotenv)