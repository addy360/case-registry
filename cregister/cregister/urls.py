from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('client/', include('client.urls')),
    path('case/', include('case.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
