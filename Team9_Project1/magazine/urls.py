from django.urls import path
from . import views
from .views import Home

urlpatterns = [
    path('', Home.as_view(), name='magazine-home'),
    path('about/', views.about, name='magazine-about'),
    path('contact/', views.contact, name='magazine-contact'),
]