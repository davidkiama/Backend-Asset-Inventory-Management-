from django.urls import path

from . import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<pk>', views.request_detail, name='request_detail'),
    path('', views.request_list, name='emp_dashboard')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
