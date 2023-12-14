from rest_framework.serializers import ModelSerializer

from .models import BestPupils, Exam, Courses


class ExamSerializer(ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class BestPupilsSerializer(ModelSerializer):
    class Meta:
        model = BestPupils
        fields = '__all__'


class CoursesSerializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

