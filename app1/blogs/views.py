from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Blog
from .forms import BlogForm

def blog_list(request):
    blogs = Blog.objects.order_by('-created_at')
    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blogs/blog_list.html', {
        'page_obj': page_obj
    })


def blog_create(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_list')

    return render(request, 'blogs/blog_create.html', {
        'form': form
    })
