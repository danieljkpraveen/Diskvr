from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.static import serve

from diskvr import settings


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('user_admin_area/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path("", include('core.urls')),
    path('inventory/', include('inventory.urls')),
] 

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
urlpatterns += [
    re_path(
        r'^media/(?P<path>.*)$',
        serve,
        {'document_root': settings.MEDIA_ROOT, }
    ),
]
