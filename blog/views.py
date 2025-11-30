from django.shortcuts import render, get_object_or_404
from .models import Post, Author

def post_list(request):
    posts = Post.objects.filter(is_published=True)
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug )
    context = {'post': post}
    return render(request, 'blog/post_detail.html', context)

def  author_detail(request, slug):
    author = get_object_or_404(Author, slug=slug)
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    context = {'posts': posts,
               'author': author}
    return render(request, 'blog/author_detail.html', context)