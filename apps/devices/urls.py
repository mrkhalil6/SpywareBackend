from django.urls import path
from . import views

urlpatterns = [
    path('', views.DeviceView.as_view()),
    path('<int:device_id>/', views.DeviceView.as_view()),
]
