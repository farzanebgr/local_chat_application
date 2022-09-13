from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('user_app.urls')),
    path('user/', include('user_app.urls')),
    path('admin/', admin.site.urls),
]