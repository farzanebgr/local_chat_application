from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from user_app.views import index_view


urlpatterns = [
    path('', index_view, name='index-page'),
    path('user/', include('user_app.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
