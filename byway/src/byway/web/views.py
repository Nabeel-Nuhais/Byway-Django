from django.shortcuts import render
from django.http.response import HttpResponse
from web.models import Categories

def index(request):
    categories = Categories.objects.all()
    
    context = {
        "categories": categories,
    }
    return render(request, "byway.html", context=context)


def courses(request):
    return render(request, "courses.html")


def single(request):
    return render(request, "single.html")