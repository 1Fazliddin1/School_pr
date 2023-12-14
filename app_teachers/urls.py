from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import TeachersModelViewSet, TradeUnionModelViewSet, LessonModelViewSet

router = DefaultRouter()


router.register(r'teacher', TeachersModelViewSet, basename='teacher')
router.register(r'union', TradeUnionModelViewSet, basename='union')
router.register(r'lesson', LessonModelViewSet, basename='lesson')


urlpatterns = []+ router.urls





# asgiref==3.7.2
# certifi==2023.11.17
# charset-normalizer==3.3.2
# coreapi==2.3.3
# coreschema==0.0.4
# Django==4.2.7
# django-cors-headers==4.3.1
# djangorestframework==3.14.0
# drf-yasg==1.21.7
# idna==3.6
# inflection==0.5.1
# itypes==1.2.0
# Jinja2==3.1.2
# MarkupSafe==2.1.3
# packaging==23.2
# Pillow==10.1.0
# psycopg2-binary==2.9.9
# PyJWT==2.8.0
# pypng==0.20220715.0
# pytz==2023.3.post1
# PyYAML==6.0.1
# qrcode==7.4.2
# requests==2.31.0
# sqlparse==0.4.4
# textwrap3==0.9.2
# typing_extensions==4.8.0
# uritemplate==4.1.1
# urllib3==2.1.0
# wcwidth==0.2.9
#
# asgiref==3.7.2
# certifi==2023.11.17
# charset-normalizer==3.3.2
# coreapi==2.3.3
# coreschema==0.0.4
# Django==4.2.7
# django-cors-headers==4.3.1
# djangorestframework==3.14.0
# drf-yasg==1.21.7
# idna==3.6
# inflection==0.5.1
# itypes==1.2.0
# Jinja2==3.1.2
# MarkupSafe==2.1.3
# packaging==23.2
# Pillow==10.1.0
# psycopg2-binary==2.9.9
# PyJWT==2.8.0
# pypng==0.20220715.0
# pytz==2023.3.post1
# PyYAML==6.0.1
# qrcode==7.4.2
# requests==2.31.0
# sqlparse==0.4.4
# textwrap3==0.9.2
# typing_extensions==4.8.0
# uritemplate==4.1.1
# urllib3==2.1.0
# wcwidth==0.2.9
#
#
