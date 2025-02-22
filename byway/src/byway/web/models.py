from django.db import models
from decimal import Decimal

LANGUAGES = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('it', 'Italian'),
    ('de', 'German'),
]

class Category(models.Model):
    title = models.CharField(max_length=100) 
    icon = models.FileField(upload_to='category_icons/')  

    def course_count(self):
        return self.courses.count()  

    def __str__(self):
        return self.title
    
    
class Language(models.Model):
    code = models.CharField(max_length=5, choices=LANGUAGES, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='course_images/')
    star_rating = models.FileField(upload_to='course_icons/', blank=True, null=True)
    instructor = models.CharField(max_length=100)
    author_icon = models.FileField(upload_to='course_icons', blank=True, null=True)
    rating = models.FloatField()
    total_ratings = models.IntegerField()
    total_hours = models.FloatField()
    total_lectures = models.IntegerField()
    level = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    languages = models.ManyToManyField(Language, blank=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    total_students = models.PositiveIntegerField(default=0)
    total_courses = models.PositiveIntegerField(default=0)  
    reviews = models.PositiveIntegerField(default=0) 
    certification = models.TextField(blank=True, null=True) 
    course_description = models.TextField(blank=True, null=True) 
    instructor_bio = models.TextField(blank=True, null=True)  

    @property
    def discounted_price(self):
        """Calculate the discounted price (50% off)"""
        return self.price * Decimal('0.5')

    def __str__(self):
        return self.title


class Instructor(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='instructors/')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    single_star = models.FileField(upload_to='instructor_icons/', blank=True, null=True)
    total_students = models.PositiveIntegerField(default=0)
    total_courses = models.PositiveIntegerField(default=0) 
    reviews = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='testimonials/')
    quote = models.TextField()

    def __str__(self):
        return self.name
    
    
class Syllabus(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='syllabus')
    title = models.CharField(max_length=200) 
    lessons = models.PositiveIntegerField() 
    duration = models.CharField(max_length=50) 

    def __str__(self):
        return f"{self.title} - {self.course.title}"


class Review(models.Model):
    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name='course_reviews'  
    )
    user_name = models.CharField(max_length=100) 
    user_image = models.ImageField(upload_to='reviews/', null=True, blank=True) 
    rating = models.PositiveIntegerField(default=1) 
    review_date = models.DateField(auto_now_add=True) 
    description = models.TextField()  

    def __str__(self):
        return f"{self.user_name} - {self.course.title} ({self.rating} stars)"


