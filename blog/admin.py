from django.contrib import admin
from .models import Author, Post
# Register your models here.
@admin.register(Author)
class Autor(admin.ModelAdmin):
    list_display = ('name', 'slug', 'email')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name', 'email')

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'slug')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}