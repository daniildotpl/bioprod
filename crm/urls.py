from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('app_site.urls')),
    path('status/', include('app_status.urls')),
    path('rearward/', include('app_rearward.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "crm.views.page_not_found_view"