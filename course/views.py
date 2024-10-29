from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Import messages for feedback
from course.models import Course

# New homepage view
def homepage(request):
    # Example: Get the first 5 courses, you can adjust the filter as needed
    featured_courses = Course.objects.all()[:5]  # Get the first 5 courses
    context = {
        "featured_courses": featured_courses
    }
    return render(request, "homepage.html", context)

@login_required
def course_list(request):
    courses = Course.objects.all()
    
    for course in courses:
        course.is_unlocked = request.user in course.subscribers.all()  # type: ignore

    context = {
        "courses": courses
    }
    return render(request, "course_list.html", context)

@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    # Check if the user is not a subscriber
    if request.user not in course.subscribers.all():
        messages.warning(request, "You need to subscribe to this course to view its details.")  # Add feedback
        return redirect("course_list")  # Redirect to the course list
    
    context = {
        "course": course
    }
    return render(request, "course_detail.html", context)

def about_us(request):
    return render(request, "about_us.html")
