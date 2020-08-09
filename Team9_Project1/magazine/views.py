from django.shortcuts import render
from .forms import ContactUsForm
from .apis import top_headlines, music
from django.views.generic import ListView
from .models import MagazinePosts


# def home(request):
#     headlines = top_headlines()
#     music_news = music()
#     context = {
#         'title': 'Home',
#         'articles': headlines,
#         'music': music_news
#     }
#     return render(request, 'magazine/home.html', context)

class Home(ListView):
    model = MagazinePosts
    template_name = 'magazine/home.html'
    headlines = top_headlines()
    music_news = music()
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = self.headlines
        context['music'] = self.music_news
        return context



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
