

from django.urls import path
from .views import HomePageView, AboutPageView #new import

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),  #new code
]
