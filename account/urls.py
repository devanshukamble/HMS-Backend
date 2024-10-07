from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("register/",views.UserRegistrationView.as_view(),name="register"),
    path("login/",views.UserLoginView.as_view(),name="login"),
    path("profile/",views.UserProfileView.as_view(),name="profile"),
    path("refreshtoken/",views.TokenRefreshView.as_view(),name="refresh"),
    path("changepassword/",views.ChangePasswordView.as_view(),name="changepassword"),
    path("sendresetpasswordemail/",views.SendResetPasswordEmailView.as_view(),name="sendresetpassword"),
    path("resetpassword/<uid>/<token>/",views.UserPasswordRestView.as_view(),name="resetpassword"),
]
