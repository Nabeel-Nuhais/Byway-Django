from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100) 
    icon = models.FileField(upload_to='category_icons/')  

    def course_count(self):
        return self.courses.count()  

    def __str__(self):
        return self.title


class Course(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')  
    title = models.CharField(max_length=200) 
    image = models.ImageField(upload_to='course_images/') 
    star_rating = models.FileField(upload_to='course_icons/', blank=True, null=True)
    instructor = models.CharField(max_length=100) 
    rating = models.FloatField() 
    total_ratings = models.IntegerField() 
    total_hours = models.FloatField()  
    total_lectures = models.IntegerField()  
    level = models.CharField(max_length=50)  
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title


class Instructor(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='instructors/')
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    single_star = models.FileField(upload_to='instructor_icons/', blank=True, null=True)
    total_students = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='testimonials/')
    quote = models.TextField()

    def __str__(self):
        return self.name