from django.urls import path
from web.views import CategoryListView, CoursesView, SingleView


app_name = "web"  

urlpatterns = [
    path("", CategoryListView.as_view(), name="index"), 
    path("all-courses/", CoursesView.as_view(), name="courses"),  
    path("single-page/", SingleView.as_view(), name="single"), 
]
