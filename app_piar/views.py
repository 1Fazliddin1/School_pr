from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

# from school_pr.app_pages.models import AboutSchool


from .models import (News,
                     Anons,
                     Vacancy,
                     Image,
                     PhotoGallery,
                     VideoGallery)

from .serializers import (NewsSerializer,
                          AnonsSerializer,
                          VacancySerializer,
                          ImagesSerializer,
                          PhotoGallerySerializer,
                          VideoGallerySerializer
                          )


class NewModelViewSet(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    def retrieve(self, request, *args, **kwargs):
        try:
            counter = News.objects.filter(pk=self.kwargs['pk']).values_list('news_views_count').first()[0]
            News.objects.filter(pk=self.kwargs['pk']).update(news_views_count=counter+1)
        except:
            pass
        return super().retrieve(request,  *args, **kwargs)


class AnonsModelViewSet(ModelViewSet):
    serializer_class = AnonsSerializer
    queryset = Anons.objects.all()


class AnonsSearchAPIView(ListAPIView):
    serializer_class = AnonsSerializer

    def get_queryset(self):
        try:
            key_word = self.kwargs['title']
            queryset = (Anons.objects.filter(anons_title_uz__icontains=key_word) |
                        Anons.objects.filter(anons_title_ru__icontains=key_word) |
                        Anons.objects.filter(anons_title_en__icontains=key_word) |
                        Anons.objects.filter(anons_desc_uz__icontains=key_word) |
                        Anons.objects.filter(anons_desc_ru__icontains=key_word) |
                        Anons.objects.filter(anons_desc_en__icontains=key_word)
                        )
        except:
            queryset = Anons.objects.none()
        return queryset


class NewsSearchAPIView(ListAPIView):
    # filter_backends = (DocSearchFiltersBackend,)
    serializer_class = NewsSerializer

    def get_queryset(self):
        try:
            key_word = self.kwargs['title']
            queryset = (News.objects.filter(news_title_uz__icontains=key_word) |
                        News.objects.filter(news_title_ru__icontains=key_word) |
                        News.objects.filter(news_title_en__icontains=key_word) |
                        News.objects.filter(news_desc_uz__icontains=key_word) |
                        News.objects.filter(news_desc_ru__icontains=key_word) |
                        News.objects.filter(news_desc_en__icontains=key_word) |
                        News.objects.filter(news_text_uz__icontains=key_word) |
                        News.objects.filter(news_text_ru__icontains=key_word) |
                        News.objects.filter(news_text_en__icontains=key_word)
                        )
        except:
            queryset = News.objects.none()
        return queryset


class VacancyModelViewSet(ModelViewSet):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Vacancy.objects.filter(vacancy_status=True)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PhotoGalleryModelViewSet(ModelViewSet):
    serializer_class = PhotoGallerySerializer
    queryset = PhotoGallery.objects.all()


class VideoGalleryModelViewSet(ModelViewSet):
    serializer_class = VideoGallerySerializer
    queryset = VideoGallery.objects.all()