from django.shortcuts import render


def home(request):
    context = {
        'title': 'Blog Home'
    }
    return render(request, 'blog/home.html', context)

