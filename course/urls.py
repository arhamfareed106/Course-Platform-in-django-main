from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("courses/", views.course_list, name="course_list"),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
    path("about-us/", views.about_us, name="about_us"),  # New About Us URL
]
