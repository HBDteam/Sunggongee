from django.urls import path
from . import views

urlpatterns = [
    path('admin_main/', views.adminMain)
]
