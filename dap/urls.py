from django.contrib import admin
# include 추가
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
import book.urls

from rest_framework import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(book.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)