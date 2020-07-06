from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="news"),
    path("Archive/", views.Archive, name="Archive"),
    path("About/", views.About, name="About"),
    path("Feedback/", views.Feedbac, name="Feedback"),
    path("Contact/", views.Contact, name="Contact"),
    path("Advertise/", views.Ads, name="Advertise"),
    path("descriptive/<int:myid>", views.Read_more, name="descriptive"),

]