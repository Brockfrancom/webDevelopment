from django.urls import path

from . import views

app_name = 'unitconv'

urlpatterns = [
    path('', views.index, name='index'),
    path('convert/', views.convert, name='convert'),
    path('init/', views.init, name='init'),
]

