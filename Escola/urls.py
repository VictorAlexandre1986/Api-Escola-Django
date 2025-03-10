"""
URL configuration for Escola project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from curso.views import CursoViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'Curso', CursoViewSet, basename='curso')

# Configuração do Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API de Cursos",
        default_version='v1',
        description="Documentação da API para gerenciamento de cursos",
        terms_of_service="https://www.seusite.com/terms/",
        contact=openapi.Contact(email="seuemail@exemplo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,  # Permite acesso público ao Swagger
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # Rotas do Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
