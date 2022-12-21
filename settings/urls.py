from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = [
    path('admins/', admin.site.urls),
    path('api/', include("api.urls")),
    path("", TemplateView.as_view(template_name="index.html"))
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
