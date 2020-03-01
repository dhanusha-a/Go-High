from django.shortcuts import render
from .models import Contact


def home(request):
    return render(request, 'index.html', {})


def login(request):
    return render(request, "login.html")


def contact(request):
    if request.method == 'POST':
        name_r = request.POST.get('Name')
        email_r = request.POST.get('Email')
        msg_r = request.POST.get('Message')
        c = Contact(Name=name_r, Email=email_r, Message=msg_r)
        c.save()
        return render(request, 'contact.html', {})
    else:
        return render(request, 'contact.html', {})

