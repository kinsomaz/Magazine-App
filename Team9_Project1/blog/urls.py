from django.urls import path
from .views import (
    blog_post_detail_view,
    blog_post_list_view,
    blog_post_update_view,
    blog_post_delete_view,
    blog_post_create_view
)

urlpatterns = [
    path('', blog_post_list_view, name='blog-home'),
    path('detail/<str:slug>/', blog_post_detail_view, name='blog-post'),
    path('edit/<str:slug>/', blog_post_update_view, name='edit-post'),
    path('delete/<str:slug>', blog_post_delete_view, name='delete-post'),
    path('create/', blog_post_create_view, name='create-post')
]
