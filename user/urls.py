from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("user/info/", views.user_info, name="user_info"),
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(next_page="course_list"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),  # Redirect to login after logout
    path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
]
