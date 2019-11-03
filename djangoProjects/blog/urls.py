from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('bio/', views.bio, name='bio'),
    path('blogArchive/', views.blogArchive, name='blogArchive'),
    path('tech/', views.tech, name='tech'),
    path('nuke/', views.nuke, name='nuke'),
    path('init/', views.init, name='init'),
    path('<int:blog_id>/comments/', views.comments, name='comments'),
]

