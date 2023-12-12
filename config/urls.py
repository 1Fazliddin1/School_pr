from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='SCHOOL site',
        description='project for school N˚ 13',
        default_version='v1',
        contact= openapi.Contact(email='omonullayevfazliddin96@gmail.com')

    ),
    public= True,
    permission_classes=(permissions.AllowAny, ),

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('users.urls')),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/pages/', include('app_pages.urls')),
    path('api/v1/piar/', include('app_piar.urls')),
    path('api/v1/search/', include('app_search.urls')),
    path('api/v1/teachers/', include('app_teachers.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0,), name='schema_swagger'),
    path('', schema_view.with_ui('swagger', cache_timeout=0,), name='schema_swagger'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, documentsroot=settings.MEDIA_ROOT )
