from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    subscribers = models.ManyToManyField(User, related_name='courses')
    
    # Add the is_featured field
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
