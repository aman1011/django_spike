from django.urls import path
from . import views

urlpatterns = [
    path('view_tables', views.view_tables, name='broomstick_list.html'),
]
