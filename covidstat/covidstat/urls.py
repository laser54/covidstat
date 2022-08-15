from rest_framework import routers

from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
# from django.conf.urls import url
from django.urls import re_path as url

from regions.views import RegionViewSet

router = routers.DefaultRouter()
router.register(r'region', RegionViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

schema_view = get_schema_view(
   openapi.Info(
      title="COVID-19 API",
      default_version='v1',
      description="Документация для приложения regions проекта Covidstat",
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="larinserg@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$',
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'),
]
