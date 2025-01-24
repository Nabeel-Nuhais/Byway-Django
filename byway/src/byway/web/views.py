from django.shortcuts import render, get_object_or_404
from .models import Category, Course, Instructor, Testimonial, Review, Syllabus


def byway(request):
    categories = Category.objects.all()
    courses = Course.objects.order_by('-rating')[:4]  # Show top-rated courses
    instructors = Instructor.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        'categories': categories,
        'courses': courses,
        'instructors': instructors,
        'testimonials': testimonials,
    }
    return render(request, 'byway.html', context)


def category_courses(request, category_id):
    selected_category = get_object_or_404(Category, id=category_id)
    courses = Course.objects.filter(category=selected_category)

    context = {
        'categories': Category.objects.all(), 
        'selected_category': selected_category,
        'courses': courses,
    }
    return render(request, 'category.html', context)


def courses(request):
    courses = Course.objects.all()

    context = {
        'courses': courses,
    }
    return render(request, 'courses.html', context)


def single_course(request, course_id):
    courses = Course.objects.order_by('-rating')[:4]  # Show top-rated courses
    course = get_object_or_404(Course, id=course_id)
    reviews = Review.objects.filter(course=course)  
    testimonials = Testimonial.objects.all()
    instructor = Instructor.objects.filter(name=course.instructor).first() if course.instructor else None
    syllabus = Syllabus.objects.filter(course=course)
    context = {
        'course': course,
        'reviews': reviews,
        'testimonials': testimonials,
        'instructor': instructor,
        'syllabus': syllabus,
        'courses': courses,
    }

    return render(request, 'single.html', context)



