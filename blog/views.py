from datetime import date

from django.shortcuts import render # type: ignore

from .models import Post



# Create your views here.

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request,"blog/index.html",{
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request,"blog/all_posts.html")

def post_detail(request, slug):
    return render(request,"blog/post_detail.html")


