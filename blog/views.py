from django.shortcuts import render
from blog.models import post
from django.utils import timezone

# Create your views here.

def blog_view(request):
    posts = post.objects.filter(published_date__lt = timezone.now())
    context = {'posts': posts}
    for post_ in posts:
       post_.counted_views += 1
       post_.save()
    return render(request, './blog/blog-home.html',context)

def blog_single(request):
    posts = post.objects.filter(published_date__lt = timezone.now())
    context = {'posts': posts}
    #post.counted_views += 1
    return render(request, './blog/blog-single.html', context)

def test(request):
    Post = post.objects.filter(published_date__lt= timezone.now())
    #Post = post.objects.all()
    context = {'Post' : Post}
    return render(request, 'test.html', context)