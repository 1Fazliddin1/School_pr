from rest_framework.serializers import ModelSerializer

from .models import Teachers, LessonDevelopments, TradeUnion


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'


class LessonSerializer(ModelSerializer):
    class Meta:
        model = LessonDevelopments
        fields = '__all__'


class TradeUnionSerializer(ModelSerializer):
    class Meta:
        model = TradeUnion
        fields = '__all__'

