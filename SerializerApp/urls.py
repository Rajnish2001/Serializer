from django.urls import path
from .import views

urlpatterns = [
    path('', views.student_details),
    path('student/', views.student_data),
]
