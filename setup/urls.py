from apps.equipments.views import *
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', include('apps.equipments.urls')),
    path('', include('apps.character.urls')),
    path('', include('apps.abilities.urls')),
    path('', include('apps.login.urls')),
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
