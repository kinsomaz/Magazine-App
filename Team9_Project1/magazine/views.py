from django.shortcuts import render
from .forms import ContactUsForm


def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'magazine/home.html', context)


def about(request):

    context = {
        'title': 'About'

    }
    return render(request, 'magazine/about.html', context)


def contact(request):
    form = ContactUsForm()
    context = {
        'title': 'Contact',
        'form': form
    }
    return render(request, 'magazine/contact.html', context)
