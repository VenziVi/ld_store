from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'LD Store'
admin.site.index_title = 'LD Adminstration'

urlpatterns = [
    path('admin/', admin.site.urls), # Admin url
    path('', include('store.urls')), # Store url
    path('cart/', include('cart.urls')), # Cart url
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
