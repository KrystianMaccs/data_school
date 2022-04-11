from django.conf import settings
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf.urls import url


schema_view = get_schema_view(
   openapi.Info(
      title="Sirius Academy",
      default_version='v1',
      description="Sirius Academy: An online learning platform",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="krystianmaccs@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    url('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url('auth/', include('djoser.urls')),
    url('auth/', include('djoser.urls.jwt')),
    url('auth/', include('djoser.social.urls')),
    url('auth/', include('djoser.urls.authtoken')),
    path('macc/', admin.site.urls),
    path('paystack/', include('paystack.urls')),
    path('profiles/', include("apps.profiles.urls")),
    #path('course/', include("apps.courses.urls")),
    #path('classroom/', include("apps.classroom.urls")),
    #path('blog/', include("apps.blog.urls")),
    #path('payments/', include("apps.payments.urls")),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Data Science School Admin"
admin.site.site_title = "Data Science School Admin Portal"
admin.site.index_title = "Welcome to the Data Science School Portal"