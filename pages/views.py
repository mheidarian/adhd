from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save message to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Send email notification
        full_message = f"""
        نام: {name}
        ایمیل: {email}
        موضوع: {subject}
        پیام: {message}
        """
        
        try:
            send_mail(
                f'تماس با ما: {subject}',
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
        except Exception:
            # Continue even if email sending fails
            pass
            
        messages.success(request, 'پیام شما با موفقیت ذخیره شد و به زودی با شما تماس خواهیم گرفت.')
        return redirect('contact')
        
    return render(request, 'pages/contact.html')
