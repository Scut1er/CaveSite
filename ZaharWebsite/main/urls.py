from django.contrib import admin
from django.urls import path
from . import views  # Импортируем ваши views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Домашняя страница
    path('about/', views.about, name='about'),  # Страница About
    path('requests/', views.requests, name='requests'),  # Страница Requests
]
