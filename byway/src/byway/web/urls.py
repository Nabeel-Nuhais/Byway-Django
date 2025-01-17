from django.urls import path
from web.views import index, courses, single


app_name = "web"


urlpatterns = [
    path("", index, name="index"),
    path("all-courses/", courses, name="courses"),
    path("single-page/", single, name="single"),
]