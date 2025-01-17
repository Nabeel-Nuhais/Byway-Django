from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
    return render(request, "byway.html")


def courses(request):
    return render(request, "courses.html")


def single(request):
    return render(request, "single.html")