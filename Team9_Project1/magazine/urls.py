from django.urls import path
from . import views
from .views import MagazineListView, MagazineDetailPostView

urlpatterns = [
    path('', MagazineListView.as_view(), name='magazine-home'),
    path('magazine_post/<int:pk>/', MagazineDetailPostView.as_view(), name='detail-post'),
    path('category/<str:category>/', views.category_view, name='category'),
    path('about/', views.about, name='magazine-about'),
    path('contact/', views.contact, name='magazine-contact'),
    path('news/', views.news, name='news'),
    path('music/', views.music_view, name='music'),
    path('magazine/search',views.serach_view, name='magsearch')
]