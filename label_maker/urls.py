from django.contrib import admin
from django.urls import path, include
from label_maker_main import urls as label_maker
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(label_maker, namespace='label_maker')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
