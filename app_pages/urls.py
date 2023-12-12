from django.urls import include, path

from .views import (SchoolInfoListViewSet,
                    PasswordChangeView,
                    PasswordResetView,
                    DocumentsViewSet,
                    DocumentsSearchAPIView,
                    )

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'infos', SchoolInfoListViewSet, basename='info')
router.register(r'docs', DocumentsViewSet, basename='docs')
router.register(r'inter-docs', DocumentsViewSet, basename='inter-docs')
# router.register(r'passwor-chan', PasswordChangeView, basename='pas-chan')

urlpatterns = router.urls
urlpatterns += [
    path('password-chan', PasswordChangeView.as_view()),
    path('password-res', PasswordResetView.as_view()),
    path('search/docs/<str:title>/', DocumentsSearchAPIView.as_view()),
]

