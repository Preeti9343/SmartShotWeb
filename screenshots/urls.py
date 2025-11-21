from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_screenshots, name='search_screenshots'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
