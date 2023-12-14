from django.contrib import admin

from .models import Exam, Courses, BestPupils


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    fields = ['exam_topic', 'exam_desc', 'exam_date', 'exam_status']
    list_display = ['id', 'exam_topic', 'exam_status', 'exam_desc']
    search_fields = ['exam_desc', 'exam_topic']


@admin.register(BestPupils)
class BestPupilsAdmin(admin.ModelAdmin):
    fields = ['pupil_first_name', 'pupil_last_name', 'pupil_information']
    list_display = ['id', 'pupil_first_name', 'pupil_information']
    search_fields = ['pupil_first_name', 'pupil_last_name', 'pupil_information']


@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    fields = ['courses_direction', 'courses_information', 'courses_price']
    list_display = ['id', 'courses_direction', 'courses_information', 'courses_price',]
    search_fields = ['courses_direction', 'courses_information', 'courses_price']
