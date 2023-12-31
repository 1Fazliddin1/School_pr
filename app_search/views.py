from rest_framework.generics import ListAPIView


from app_pages.models import Documents, InternalDocs
from app_pages.serializers import DocumentsSerializer

from app_piar.models import News, Anons, Vacancy, PhotoGallery, VideoGallery
from app_piar.serializers import (NewsSerializer,
                                  AnonsSerializer,
                                  VacancySerializer,
                                  PhotoGallerySerializer,
                                  VideoGallerySerializer)


serializers_list = {'docs': DocumentsSerializer,
                    'news': NewsSerializer,
                    'anons': AnonsSerializer,
                    'vacancy': VacancySerializer,
                    'photos': PhotoGallerySerializer,
                    'videos': VideoGallerySerializer}

models_list = [Documents, InternalDocs, News, Anons, Vacancy, PhotoGallery, VideoGallery]


class UniversalSearchListAPIView(ListAPIView):
    def get_serializer_class(self):
        try:
            col_name = self.request.GET['where']
            if col_name in serializers_list.keys():
                return serializers_list[col_name]
        except:
            return NewsSerializer

    def get_queryset(self):
        try:
            col_name = self.request.GET['where']
            key_word = self.request.GET['keyword']
            match col_name:
                case 'news':
                    queryset = (News.objects.filter(news_title_uz__icontains=key_word) |
                                News.objects.filter(news_title_ru__icontains=key_word) |
                                News.objects.filter(news_title_en__icontains=key_word) |
                                News.objects.filter(news_desc_uz__icontains=key_word) |
                                News.objects.filter(news_desc_ru__icontains=key_word) |
                                News.objects.filter(news_desc_en__icontains=key_word) |
                                News.objects.filter(news_text_uz__icontains=key_word) |
                                News.objects.filter(news_text_ru__icontains=key_word) |
                                News.objects.filter(news_text_en__icontains=key_word))
                    return queryset
                case 'anons':
                    queryset = (Anons.objects.filter(anons_title_uz__icontains=key_word) |
                                Anons.objects.filter(anons_title_ru__icontains=key_word) |
                                Anons.objects.filter(anons_title_en__icontains=key_word) |
                                Anons.objects.filter(anons_desc_uz__icontains=key_word) |
                                Anons.objects.filter(anons_desc_ru__icontains=key_word) |
                                Anons.objects.filter(anons_desc_en__icontains=key_word))
                    return queryset
                case 'docs':
                    queryset = (Documents.objects.filter(doc_title_uz__icontains=key_word) |
                                Documents.objects.filter(doc_title_ru__icontains=key_word) |
                                Documents.objects.filter(doc_title_en__icontains=key_word) |
                                Documents.objects.filter(doc_code__icontains=key_word))
                    return queryset
                case 'vacancy':
                    queryset = (Vacancy.objects.filter(vacancy_name_uz__icontains=key_word, vacancy_status=True) |
                                Vacancy.objects.filter(vacancy_name_ru__icontains=key_word, vacancy_status=True) |
                                Vacancy.objects.filter(vacancy_name_en__icontains=key_word, vacancy_status=True) |
                                Vacancy.objects.filter(vacancy_desc_uz__icontains=key_word, vacancy_status=True) |
                                Vacancy.objects.filter(vacancy_desc_ru__icontains=key_word, vacancy_status=True) |
                                Vacancy.objects.filter(vacancy_desc_en__icontains=key_word, vacancy_status=True) |
                                Vacancy.objects.filter(vacancy_text_uz__icontains=key_word, vacancy_status=True) |
                                Vacancy.objects.filter(vacancy_text_ru__icontains=key_word, vacancy_status=True) |
                                Vacancy.objects.filter(vacancy_text_en__icontains=key_word, vacancy_status=True))
                    # queryset = queryset.filter(vacancy_status=True)
                    return queryset
                case 'photos':
                    queryset = (PhotoGallery.objects.filter(gallery_title_uz__icontains=key_word) |
                                PhotoGallery.objects.filter(gallery_title_ru__icontains=key_word) |
                                PhotoGallery.objects.filter(gallery_title_en__icontains=key_word) |
                                PhotoGallery.objects.filter(gallery_desc_uz__icontains=key_word) |
                                PhotoGallery.objects.filter(gallery_desc_ru__icontains=key_word) |
                                PhotoGallery.objects.filter(gallery_desc_en__icontains=key_word))
                    return queryset
                case 'videos':
                    queryset = (VideoGallery.objects.filter(gallery_title_uz__icontains=key_word) |
                                VideoGallery.objects.filter(gallery_title_ru__icontains=key_word) |
                                VideoGallery.objects.filter(gallery_title_en__icontains=key_word) |
                                VideoGallery.objects.filter(gallery_desc_uz__icontains=key_word) |
                                VideoGallery.objects.filter(gallery_desc_ru__icontains=key_word) |
                                VideoGallery.objects.filter(gallery_desc_en__icontains=key_word))
                    return queryset
                case _:
                    return News.objects.none()
        except:
            return News.objects.none()
