from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='magazine-home'),
    path('about/', views.about, name='magazine-about'),
    path('contact/', views.contact, name='magazine-contact'),
]
