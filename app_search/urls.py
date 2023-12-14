from django.urls import path

from .views import UniversalSearchListAPIView

urlpatterns = [
    path('', UniversalSearchListAPIView.as_view())
]