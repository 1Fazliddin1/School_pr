from django.db import models


class BestPupils(models.Model):
    pupil_first_name = models.CharField(max_length=50, verbose_name='O`quvchining ismi')
    pupil_last_name = models.CharField(max_length=50, verbose_name='O`quvchining familiyasi')
    pupil_information = models.TextField(verbose_name='O`quvchi haqida malumot')

    def __str__(self):
        return self.pupil_first_name

    class Meta:
        db_table = 'Best_pupil_info'


class Exam(models.Model):
    exam_topic = models.CharField(max_length=50, verbose_name='IMTHON mavzusi')
    exam_desc = models.CharField(max_length=255, verbose_name='IMTHON qoidalari')
    exam_date = models.DateField(verbose_name='IMTHON boshlanish vaqti')
    exam_status = models.BooleanField(verbose_name='IMTHON holati', default=True)

    def __str__(self):
        return self.exam_topic

    class Meta:
        db_table = 'Exam'


class Courses(models.Model):
    courses_direction = models.CharField(max_length=50, verbose_name='Kurs yo`nalishi')
    courses_information = models.TextField(verbose_name='Kurs haqida malumot malumot')
    courses_price = models.CharField(max_length=50, verbose_name='Kurs narxi')

    def __str__(self):
        return self.courses_direction

    class Meta:
        db_table = 'Courses'
