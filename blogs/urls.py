from django.urls import path

from . import views


app_name = 'blogs'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('blogs/', views.blogs, name = 'blogs'),
    path('blogs/<int:blog_id>/', views.blog, name = 'blog'),
    path('blogs/new_blog/', views.new_blog, name = 'new_blog'),
    path('blogs/<int:blog_id>/new_post/', views.new_post, name = 'new_post'),
    path('blogs/<int:blog_id>/edit_blog/', views.edit_blog, name = 'edit_blog'),
    path('blogs/edit_post/<int:post_id>/', views.edit_post, name = 'edit_post'),
]