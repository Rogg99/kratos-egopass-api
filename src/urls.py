
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions                                                                                                                                                                             
from django.conf import settings
from django.conf.urls.static import static

schema_view2 = get_schema_view(
    openapi.Info(
        title="KRATOS payment API",
        default_version='v1',
        description="KRATOS payment API",
        contact=openapi.Contact(email="info@payment.com"),

    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
    path('kratos-payment/api/', schema_view2.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('kratos-payment/api/admin/', admin.site.urls),
    path('kratos-payment/api/doc/swagger/', schema_view2.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('kratos-payment/api/v1/auth/', include('apps.authentication.urls')),
    path('kratos-payment/api/v1/api/', include('apps.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
