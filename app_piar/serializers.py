from rest_framework.serializers import ModelSerializer

from .models import (News,
                     Anons,
                     Vacancy,
                     Image,
                     PhotoGallery,
                     YoutubeLinks,
                     VideoGallery)


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        read_only_fields = ('news_views_count', )
        fields = '__all__'


class AnonsSerializer(ModelSerializer):
    class Meta:
        model = Anons
        fields = '__all__'


class VacancySerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        # read_only_fields = ('news_views_count', )
        fields = '__all__'


class ImagesSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class PhotoGallerySerializer(ModelSerializer):
    gallery_images = ImagesSerializer(many=True, read_only=True)

    class Meta:
        model = PhotoGallery
        read_only_fields = ['gallery_view_count']
        fields = '__all__'


class VideosSerializer(ModelSerializer):
    class Meta:
        model = YoutubeLinks
        fields = '__all__'


class VideoGallerySerializer(ModelSerializer):
    gallery_images = VideosSerializer(many=True, read_only=True)

    class Meta:
        model = VideoGallery
        read_only_fields = ['gallery_view_count']
        fields = '__all__'


