from django.contrib import admin
from .models import Category, Course, Instructor, Testimonial, Language, Syllabus, Review


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'course_count']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'rating', 'price']


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'rating', 'total_students', 'total_courses']


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role']


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'code']
    
    
@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'lessons', 'duration']
    list_filter = ['course']
    
    
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'course', 'rating', 'review_date']
    list_filter = ['course', 'rating']
    search_fields = ['user_name', 'description']

