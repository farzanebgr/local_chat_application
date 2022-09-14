from django.urls import path
from user_app import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register-page'),
    path('login/', views.LoginView.as_view(), name='login-page'),
]