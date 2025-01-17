from django.db import models


class Categories(models.Model):
    icon = models.FileField(upload_to="svg_icons/")
    title = models.CharField(max_length=128)
    course_count = models.CharField(max_length=128)
    
    
    class Meta:
        db_table = "web_categories"
        ordering = ["id"]
        verbose_name = "categorie"
        
    def __str__(self):
        return str(self.id)
