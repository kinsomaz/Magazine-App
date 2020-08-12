from django.shortcuts import render, redirect
from .forms import ContactUsForm
from .apis import top_headlines, search
from django.views.generic import ListView, DetailView
from .models import MagazinePosts
from decouple import config
api_key = config('api_key')


class MagazineListView(ListView):
    model = MagazinePosts
    template_name = 'magazine/home.html'
    headlines = top_headlines(page=1, page_size=5, api_key=api_key)
    music_news = search(page=1, page_size=5, api_key=api_key, query='music')
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = self.headlines
        context['music'] = self.music_news
        return context


class MagazineDetailPostView(DetailView):
    model = MagazinePosts
    template_name = 'magazine/post.html'
    context_object_name = 'post'


def category_view(request, category):
    context = {
        'posts': MagazinePosts.objects.filter(category=category),
        'category': category
    }

    return render(request,'magazine/category.html', context)


def about(request):
    context = {
        'title': 'About'

    }
    return render(request, 'magazine/about.html', context)


def contact(request):
    form = ContactUsForm()
    context = {
        'title': 'Contact',
        'form': form,
    }
    return render(request, 'magazine/contact.html', context)


def news(request):
    headlines = top_headlines(page=1, page_size=100, api_key=api_key)
    context = {
        'articles': headlines
    }
    return render(request, 'magazine/news.html', context)


def music_view(request):
    music_news = search(page=1, page_size=100, api_key=api_key, query='music')
    context = {
        'articles': music_news
    }
    return render(request, 'magazine/music.html', context)

def serach_view(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        res = search(1, 100, query, api_key)
        context = {
            'articles': res,
            'query': query
        }
        return render(request, 'magazine/search.html',context)
    else:
        return redirect(MagazineListView.as_view())