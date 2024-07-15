from datetime import date

from django.shortcuts import render # type: ignore

posts=[
    {
        "slug": "hike-in-the-mountains",
        "images": "django_3.jpg",
        "author": "Vaishnavi",
        "date": date(2024, 7, 15),
        "title": "Mountain Hiking",
        "excerpt" : "Mountains are prominent landforms formed by tectonic forces or volcanism, offering diverse ecosystems and stunning landscapes.",
        "content": """
                    Mountains are prominent landforms formed by tectonic forces or volcanism, offering diverse ecosystems and stunning landscapes
                    Mountains are prominent landforms formed by tectonic forces or volcanism, offering diverse ecosystems and stunning landscapes
                    Mountains are prominent landforms formed by tectonic forces or volcanism, offering diverse ecosystems and stunning landscapes
"""
    }
]

# Create your views here.

def starting_page(request):
    return render(request,"blog/index.html")

def posts(request):
    return render(request,"blog/all_posts.html")

def post_detail(request, slug):
    return render(request,"blog/post_detail.html")


