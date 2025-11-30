from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # исправлено 'objects'
    context = {'posts': posts}  # context должен быть словарём
    return render(request, 'post_list.html', context)  # возвращаем результат

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)  # безопасно получаем объект
    context = {'post': post}
    return render(request, 'post_detail.html', context)
