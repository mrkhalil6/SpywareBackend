from django.urls import path
from . import views

urlpatterns = [
    path('', views.SMSView.as_view()),
    path('<int:sms_id>/', views.SMSView.as_view()),
    path('conversations/', views.ConversationView.as_view()),
    path('conversations/<str:address>', views.ChatView.as_view()),
]
