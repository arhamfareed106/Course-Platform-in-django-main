from django.contrib import admin
from .models import Course
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor','created_at','update_at',]
    search_fields= ['title','instructor__username',]
    list_filter=["created_at", "update_at","instructor",]
