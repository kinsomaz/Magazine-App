from django.shortcuts import render


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
    context = {
        'title': 'Contact'
    }
    return render(request, 'magazine/contact.html', context)
