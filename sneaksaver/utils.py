from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from django.conf import settings
import os


def upload_location(instance, filename):
    file_path = 'product/product_{cid}.jpeg'.format(
        cid=str(instance.slug), filename=filename
    )
    full_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if os.path.exists(full_path):
        os.remove(full_path)
    return file_path

def send_email_view(email, subject, message):
    # Your view logic here

    # Send email
    from_email = settings.DEFAULT_FROM_EMAIL

    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=[email,])

    # Optionally, you can handle success or failure
    return HttpResponse('Email sent successfully!')