from django.contrib import admin
from .models import Author, Post
# Register your models here.
@admin.register(Author)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'email')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ('name', 'email')


@admin.action(description='Опубликовать выбранные посты')
def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)

@admin.action(description='Снять с публикации выбранные посты')
def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'slug', 'is_published')
    list_filter = ('author', 'created_at', 'is_published')
    list_editable = ('is_published', )
    search_fields = ('title', 'content')
    list_per_page = 5
    prepopulated_fields = {"slug": ("title",)}
    actions = [make_published, make_unpublished]

  
