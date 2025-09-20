from django.urls import path, include
from rest_framework import routers
from django.contrib import admin
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
       title="Documentação da API",
      default_version='v1',
      description="Documentação da API do projeto BD",
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)

router = routers.DefaultRouter()

urlpatterns = [
    path('', include('apps.equipments.urls')),
    path('', include('apps.character.urls')),
    path('', include('apps.abilities.urls')),
    path('', include('apps.login.urls')),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
]
