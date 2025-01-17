from django.contrib import admin
from web.models import Categories


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "icon", "title", "course_count"]
    
admin.site.register(Categories, CategoryAdmin)

