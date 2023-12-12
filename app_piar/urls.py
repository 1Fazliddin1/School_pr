from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (NewModelViewSet,
                    NewsSearchAPIView,
                    AnonsModelViewSet,
                    AnonsSearchAPIView,
                    VacancyModelViewSet,
                    PhotoGalleryModelViewSet,
                    VideoGalleryModelViewSet
                    )


router = DefaultRouter()

router.register(r'news', NewModelViewSet, basename='news')
router.register(r'anons', AnonsModelViewSet, basename='anons')
router.register(r'vacancy', VacancyModelViewSet, basename='vacancy')
router.register(r'photos', PhotoGalleryModelViewSet, basename='photos')
router.register(r'videos', VideoGalleryModelViewSet, basename='videos')

# urlpatterns = router.urls
urlpatterns = [
    path('search/new/<str:title>/', NewsSearchAPIView.as_view()),
    path('search/anon/<str:title>/', AnonsSearchAPIView.as_view()),
] + router.urls