from django.urls import path
from . import views 

app_name = "payment"  # Added namespace for easier reverse lookup

urlpatterns = [
    path("create_checkout_session/<int:course_id>/", views.create_checkout_session, name="create_checkout_session"),
    path("course_success/<int:course_id>/", views.course_success, name="course_success"),
    path("course_cancel/", views.course_cancel, name="course_cancel"),
    path("stripe/webhook/", views.stripe_webhook, name="stripe_webhook")
]
