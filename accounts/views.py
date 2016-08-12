from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render

from django.contrib import messages

from accounts.models import Token

def send_login_email(request):
    email = request.POST['email']
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token={uid}'.format(uid=token.uid))
    send_mail(
        'Your login link for Superlists',
        'Use this link to log in\n\n{url}'.format(url=url),
        'noreply@superlists',
        [email],
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')

def login(request):
    return redirect('/')
