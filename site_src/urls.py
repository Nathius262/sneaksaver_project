from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('account/', include('user.urls')),
    path('', include('sneaksaver.urls')),
    path('sneakers/', include('sneakers_image_recog.urls')),
    path('', include('data_analysis.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)