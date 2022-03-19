from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('macc/', admin.site.urls),
    path('paystack/', include('paystack.urls')),
    path('agora/',Agora.as_view(
    app_id='<APP_ID>',
    channel='<CHANNEL_ID>'
)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Data Science School Admin"
admin.site.site_title = "Data Science School Admin Portal"
admin.site.index_title = "Welcome to the Data Science School Portal"