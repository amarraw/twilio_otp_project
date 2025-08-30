# users/views.py
from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import CustomUser
from twilio.rest import Client
import random
from django.conf import settings

otp_store = {}  # Temporary store for OTPs

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate until OTP verification
            user.save()
            send_otp(user.phone_number)
            request.session['phone_number'] = user.phone_number
            return redirect('verify_otp')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def send_otp(phone):
    otp = random.randint(100000, 999999)
    otp_store[phone] = otp
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=f"Your OTP is: {otp}",
        from_=settings.TWILIO_PHONE_NUMBER,
        to=phone
    )

def verify_otp(request):
    phone = request.session.get('phone_number')
    if request.method == "POST":
        entered_otp = request.POST.get('otp')
        if phone in otp_store and str(otp_store[phone]) == entered_otp:
            user = CustomUser.objects.get(phone_number=phone)
            user.is_active = True
            user.is_verified = True
            user.save()
            otp_store.pop(phone)
            return redirect('login')
        else:
            return render(request, 'users/verify_otp.html', {'error': "Invalid OTP"})
    return render(request, 'users/verify_otp.html')
