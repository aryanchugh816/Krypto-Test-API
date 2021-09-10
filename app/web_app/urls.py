from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# from upload.views import image_upload
from rest_framework import permissions
from django.http import JsonResponse
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Krypto test API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.ourapp.com/policies/terms/",
      contact=openapi.Contact(email="contact@bmapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

def home(request):
    return JsonResponse({"hello": "world! This is Aryan Chugh's website"})


urlpatterns = [
    path('api/home/', home, name='home'),
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path("admin/", admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/event/', include('events.urls')),
    path('api/ht/', include('health_check.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
