from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from crop_image.views import main_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name="main-view")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)