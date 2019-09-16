from django.urls import path
from . import views




urlpatterns = [
    path('', views.index, name='index'),
    path('process_money',views.process_money),
    path('clear',views.clear),
]