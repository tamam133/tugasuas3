from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('blog/', include('blog.urls')),
    path('contak/', include('contak.urls')),
    path('bisnis/', include('bisnis.urls')),
]
