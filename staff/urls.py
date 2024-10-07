from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("getdoctors/",views.GetDoctorsView.as_view(),name="register"),
]
