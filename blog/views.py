from django.shortcuts import render
from blog.models import post
from django.utils import timezone

# Create your views here.

def blog_view(request):
    posts = post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, './blog/blog-home.html',context)

def blog_single(request):
    return render(request, './blog/blog-single.html')

def test(request):
    Post = post.objects.filter(published_date__gt= timezone.now())
    #Post = post.objects.all()
    context = {'Post' : Post}
    return render(request, 'test.html', context)