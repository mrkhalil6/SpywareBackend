from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactsView.as_view()),
    path('<int:contacts_id>/', views.ContactsView.as_view()),
]
