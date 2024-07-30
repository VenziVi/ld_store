from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # Admin url
    path('', include('store.urls')), # Store url
    path('cart/', include('cart.urls')), # Cart url
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
