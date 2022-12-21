from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
import django


def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)


def custom_server_error(request):
    return django.views.defaults.server_error(request)


urlpatterns = [
    path('admins/', admin.site.urls),
    path('api/', include("api.urls")),
    path("", TemplateView.as_view(template_name="index.html")),
    path("404/", custom_page_not_found),
    path("500/", custom_server_error),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
