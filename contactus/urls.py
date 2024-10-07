from django.urls import path
from . import views
urlpatterns = [
    path('contactus/',views.InsertContactUsView.as_view(),name='contactus'),
    path('newsleter/',views.SendNewsletterEmailView.as_view(),name='contactus')
]
