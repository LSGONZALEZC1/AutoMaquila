# autoMaquila/urls.py

from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('login/', include('apps.login.urls')),
    path('orders/', include('apps.orders.urls')),
    path('calzado/', include('calzado.urls')),
    path('inventario/', include('inventario.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

