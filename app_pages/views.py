from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView


from .serializers import SchoolInfoSerializer, PasswordChangeSerializer, PasswordResetSerializer, DocumentsSerializer, InternalDocsSerializer
from .models import AboutSchool, Documents
from .filters import DocSearchFiltersBackend

from rest_framework import viewsets, status
from rest_framework.response import Response

from django.contrib.auth import authenticate, login, get_user_model


class SchoolInfoListViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolInfoSerializer
    queryset = AboutSchool.objects.all()


class PasswordChangeView(APIView):
    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, username=request.user.username, password=serializer.validated_data['old_password'])
            if user is not None:
                user.set_password(serializer.validated_data['new_password'])
                user.save()
                return Response(f"Parol muvaffaqiyati ozgartiriladi")
            else:
                return Response(f"eski parol notogri")
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordResetView(APIView):
    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'message': 'User with this email does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
            token = default_token_generator.make_token(user)
            reset_link = f"https://yourdomain.com/reset-password/{user.id}/{token}/"
            send_mail(
                'Password Reset',
                f'Click the following link to reset your password: {reset_link}',
                'noreply@yourdomain.com',
                [email],
                fail_silently=False,
            )
            return Response({'message': 'Password reset link has been sent to your email.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DocumentsViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentsSerializer
    queryset = Documents.objects.all()


class InternalDocsViewSet(viewsets.ModelViewSet):
    serializer_class = InternalDocsSerializer
    queryset = Documents.objects.all()


class DocumentsSearchAPIView(ListAPIView):
    # filter_backends = (DocSearchFiltersBackend,)
    serializer_class = DocumentsSerializer

    def get_queryset(self):
            try:
                key_word = self.kwargs['title']
                sey_word = self.kwargs['title']
                queryset = Documents.objects.filter(doc_title_uz__icontains=key_word) | Documents.objects.filter(doc_title_ru__icontains=key_word) | Documents.objects.filter(doc_title_en__icontains=key_word) | Documents.objects.filter(doc_code__icontains=sey_word)
            except:
                return Documents.objects.none()
            return queryset
            # return Documents.objects.none()


