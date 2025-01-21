from django.urls import path
from . import views


app_name = 'web'

urlpatterns = [
    path('', views.byway, name='byway'),
    path('category/<int:category_id>/', views.category_courses, name='category_courses'),  # Category-specific page
    path('courses/', views.courses, name='courses'),
    path('courses/<int:course_id>/', views.single_course, name='single_course'),
]