from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TeachersModelViewSet, TradeUnionModelViewSet, LessonModelViewSet

router = DefaultRouter()


router.register(r'teacher', TeachersModelViewSet, basename='teacher')
router.register(r'union', TradeUnionModelViewSet, basename='union')
router.register(r'lesson', LessonModelViewSet, basename='lesson')


urlpatterns = []+ router.urls