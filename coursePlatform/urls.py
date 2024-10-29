
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("course.urls")),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('payment/', include('payment.urls')),
    path('course/', include('course.urls')),
]
