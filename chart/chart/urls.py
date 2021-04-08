from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chart/', include('graph.urls')),
    path('covid/', include('covid.urls')),
]
