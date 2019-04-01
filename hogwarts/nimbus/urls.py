from django.urls import path
from . import views

urlpatterns = [
    path('', views.checking_dynamodb, name='broomstick_list.html'),
]
