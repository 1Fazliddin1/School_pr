from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Exam, BestPupils, Courses
from .serializers import ExamSerializer, BestPupilsSerializer, CoursesSerializer


class ExamModelViewSet(ModelViewSet):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class BestPupilsModelViewSet(ModelViewSet):
    serializer_class = BestPupilsSerializer
    queryset = BestPupils.objects.all()


class CoursesModelViewSet(ModelViewSet):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()