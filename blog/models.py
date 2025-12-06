from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Author (models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    email = models.EmailField(max_length=254)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'
        
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    is_published = models.BooleanField(choices=tuple( map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name='Статус')

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    
