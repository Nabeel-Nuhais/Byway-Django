from django.contrib import admin
from .models import Category, Course, Instructor, Testimonial


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'course_count')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'instructor', 'price', 'rating')
    list_filter = ('category',)
    search_fields = ('title', 'instructor')
    
    
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'rating', 'total_students')
    search_fields = ('name', 'role')
    list_filter = ('role',)
    
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
    search_fields = ('name', 'role')
