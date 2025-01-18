from django.contrib import admin
from web.models import Category, Course, Instructor, Testimonial


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "icon", "title", "course_count"]  # Display columns in list view
    search_fields = ['title', 'course_count']  # Add search functionality
    list_filter = ['course_count']  # Add filtering by course_count
    ordering = ['id']  # Order categories by ID by default


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'instructor', 'rating', 'total_ratings', 'total_hours', 'price', 'level'] 
    search_fields = ['title', 'instructor', 'level'] 
    list_filter = ['level', 'price'] 
    ordering = ['id'] 
    
    
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'rating', 'total_students'] 
    search_fields = ['name', 'name', 'role'] 
    list_filter = ['rating', 'total_students'] 
    ordering = ['id'] 


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'quote']  
    search_fields = ['name', 'role', 'quote']  
    list_filter = ['role']  
    ordering = ['id']  


# Register the models with admin site
admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
