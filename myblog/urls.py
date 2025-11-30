from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_list, name='home'),  # главная страница
    path('admin/', admin.site.urls),
    path('post/', views.post_list, name='post_list'),  # список постов
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('author/<slug:slug>/', views.author_detail, name='author_detail'),
]
