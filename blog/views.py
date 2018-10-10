from django.shortcuts import render
from .models import WpPosts


# Create your views here.


def blog_home(request):
    posts = WpPosts.objects.filter(post_type='post')
    return render(request, 'home.html', {'posts': posts})


def post_detail(request, id):

    post = WpPosts.objects.get(pk=id)
    return render(request, 'detail.html', {'post': post})
