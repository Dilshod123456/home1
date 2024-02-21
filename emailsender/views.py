from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# from django.core.mail import EmailMessage

# Create your views here.
def send_email(request):
    subject = 'SPASIBO ZA REGISTRATION'
    message = 'BU SMS SIZ UCHUN'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['tuygunoff4545@gmail.com',]


    # mail = EmailMessage(subject, message, email_from, recipient_list)
    # mail.attach_file('11.jpg')
    # mail.send()
    # form = 1
    # return render (request, 'send_email.html', context={'form': form})



    send_mail(subject, message, email_from, recipient_list)
    return render (request, 'send_email.html')