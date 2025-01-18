from django.views.generic import TemplateView, ListView
from web.models import Category, Course, Instructor, Testimonial

class CategoryListView(TemplateView):  # Change to TemplateView since we are not using the default queryset of ListView
    template_name = "byway.html"

    def get_context_data(self, **kwargs):
        # Add both Category and Course data to the context
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['courses'] = Course.objects.all()
        context['instructors'] = Instructor.objects.all()
        context['testimonials'] = Testimonial.objects.all()
        return context


class CoursesView(TemplateView):
    template_name = "courses.html"


class SingleView(TemplateView):
    template_name = "single.html"
