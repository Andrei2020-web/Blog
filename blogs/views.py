from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.
def index(request):
    """Представление домашней страницы."""
    blog_posts = BlogPost.objects.order_by('date_added')
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_blog_post(request):
    """Представление странцы добавления нового сообщения."""
    if request.method != 'POST':
        """Данные не отправлялись, создаём пустую форму."""
        form = BlogPostForm()
    else:
        """Отправлены данные, обработать данные."""
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.owner = request.user
            blog_post.save()
            return redirect('blogs:index')

    """Вывести пустую или недействительную форму."""
    context = {'form': form}
    return render(request, 'blogs/new_blog_post.html', context)


def blog_post(request, blog_post_id):
    """Представление страницы сообщения."""
    blog_post = BlogPost.objects.get(id=blog_post_id)
    context = {'blog_post': blog_post}
    return render(request, 'blogs/blog_post.html', context)

@login_required
def edit_blog_post(request, blog_post_id):
    """Представление страницы для редактирования сообщения."""
    blog_post = BlogPost.objects.get(id=blog_post_id)
    if request.method != 'POST':
        """Данные не отправлялись, получаем данные из БД."""
        form = BlogPostForm(instance=blog_post)
    else:
        """Данные отправлены, сохранить данные."""
        form = BlogPostForm(instance=blog_post, data=request.POST)
        if form.is_valid():
            if blog_post.owner != request.user:
                raise Http404
            form.save()
            return redirect('blogs:index')

    content = {'form': form, 'blog_post': blog_post}
    return render(request, 'blogs/edit_blog_post.html', content)
