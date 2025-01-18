from django.db import models


class Category(models.Model):
    icon = models.FileField(upload_to="svg_icons/")
    title = models.CharField(max_length=128)
    course_count = models.PositiveIntegerField(default=0, help_text="Total number of course count")
    
    
    class Meta:
        db_table = "web_categories"
        ordering = ["id"]
        verbose_name = "categorie"
        
    def __str__(self):
        return str(self.id)
    

class Course(models.Model):
    image = models.ImageField(upload_to="courses/images/", blank=False, null=False)
    title = models.CharField(max_length=128, blank=False)
    instructor = models.CharField(max_length=128, blank=False)
    rating = models.FloatField(default=0.0, help_text="Course rating out of 5.0")
    total_ratings = models.PositiveIntegerField(default=0, help_text="Total number of ratings")
    total_hours = models.PositiveIntegerField(help_text="Total hours of the courses")
    total_lectures = models.PositiveIntegerField(help_text="Number of lecture in the course")
    level = models.CharField(
        max_length=32,
        choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')],
        default='Beginner',
    )
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="Price of the course")
    star_icon = models.FileField(upload_to="courses/icons/", blank=True, null=True)
    
    class Meta:
        db_table = "web_courses"
        ordering = ["id"]
        
    def __str__(self):
        return self.title
    
    
class Instructor(models.Model):
    image = models.ImageField(upload_to="instructors/images/", blank=False, null=False)
    name = models.CharField(max_length=128, blank=False)
    role = models.CharField(max_length=128, blank=False)
    single_star = models.FileField(upload_to="instructor/icons/")
    rating = models.FloatField(default=0.0, help_text="Instructor rating out of 5.0")
    total_students = models.PositiveIntegerField(help_text="Total number of students taught")

    class Meta:
        db_table = "web_instructors"
        ordering = ["id"]
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"

    def __str__(self):
        return self.name


from django.db import models

class Testimonial(models.Model):
    quote = models.TextField(help_text="Testimonial quote provided by the user.")
    image = models.ImageField(upload_to="testimonials/images/", blank=False, null=False)
    name = models.CharField(max_length=128, blank=False, help_text="Name of the person giving the testimonial.")
    role = models.CharField(max_length=128, blank=False, help_text="Role or designation of the reviewer.")
    
    class Meta:
        db_table = "testimonials"
        ordering = ["id"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    
    def __str__(self):
        return f"{self.name} - {self.role}"







