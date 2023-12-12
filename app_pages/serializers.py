from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import AboutSchool, Documents, InternalDocs


class SchoolInfoSerializer(ModelSerializer):
    class Meta:
        model = AboutSchool
        fields = '__all__'


class DocumentsSerializer(ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'


class InternalDocsSerializer(ModelSerializer):
    class Meta:
        model = InternalDocs
        fields = '__all__'


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)