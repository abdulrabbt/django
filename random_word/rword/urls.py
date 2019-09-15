from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('increment', views.increment),
    path('clear', views.clear),
]