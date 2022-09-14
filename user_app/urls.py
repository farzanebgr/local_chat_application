from django.urls import path
from user_app import views

urlpatterns = [
    path('', views.index_view, name='index-page'),
    path('register/', views.RegisterView.as_view(), name='register-page'),
]