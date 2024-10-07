from django.urls import path
from . import views

urlpatterns = [
    path('bookappoinment/',views.SetUserAppoinmentView.as_view(),name="bookappoinment"),
    path('viewappoinment/',views.GetUserAppoinmentView.as_view(),name="viewappoinment"),
    path('bookdoctorappoinment/',views.SetDoctorAppoinmentView.as_view(),name="bookdoctorappoinment"),
    path('viewdoctorappoinment/',views.GetDoctorAppoinmentView.as_view(),name="viewdoctorappoinment"),
] 
 