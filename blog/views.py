from django.shortcuts import render, get_object_or_404
from blog.models import post
from django.utils import timezone

# Create your views here.

def blog_view(request):
    posts = post.objects.filter(published_date__lt = timezone.now())
    context = {'posts': posts}
    return render(request, './blog/blog-home.html',context)

def blog_single(request, pid):
    Post = get_object_or_404(post, pk=pid, status = 1)
    context = {'Post':Post, 'pid':pid}
    Post.counted_views += 1
    Post.save()

    return render(request, './blog/blog-single.html', context)

def test(request, pid):
    context = {'pid':pid}
    return render(request, 'test.html', context)