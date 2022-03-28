from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('macc/', admin.site.urls),
    path('paystack/', include('paystack.urls')),
    path('course/', include('courses.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Data Science School Admin"
admin.site.site_title = "Data Science School Admin Portal"
admin.site.index_title = "Welcome to the Data Science School Portal"