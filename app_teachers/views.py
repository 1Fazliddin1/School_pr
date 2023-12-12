from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Teachers, LessonDevelopments, TradeUnion
from .serializers import TeacherSerializer, LessonSerializer, TradeUnionSerializer


class TeachersModelViewSet(ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teachers.objects.all()


class LessonModelViewSet(ModelViewSet):
    serializer_class = LessonSerializer
    queryset = LessonDevelopments.objects.all()


class TradeUnionModelViewSet(ModelViewSet):
    serializer_class = TradeUnionSerializer
    queryset = TradeUnion.objects.all()