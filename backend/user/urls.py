from django.urls import path
from .views import HealthCheck, RetriveUserView, RegisterView

urlpatterns = [
    path("health/", HealthCheck.as_view()),
    path("me/", RetriveUserView.as_view()),
    path("register/", RegisterView.as_view()),
]