from django.urls import path
from .views import model_list

urlpatterns = [
    path('', model_list, name='model_list')
    ]
