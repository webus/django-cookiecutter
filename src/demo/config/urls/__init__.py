from django.contrib import admin
from django.urls import path
from config.urls import rest

urlpatterns = [
    path('admin/', admin.site.urls),
] + rest.urlpatterns
