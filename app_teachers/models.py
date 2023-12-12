from django.db import models


class Teachers(models.Model):
    teach_first_name = models.CharField(max_length=50, verbose_name='Teacher name')
    teach_last_name = models.CharField(max_length=50, verbose_name='Teacher last')
    teach_specialist = models.CharField(max_length=50, verbose_name='mutahasisligi')
    teach_informations = models.TextField(verbose_name='O`qituvchi haqida malumot')

    def __str__(self):
        return self.teach_first_name

    class Meta:
        db_table = 'teachers_info'


class Category(models.Model):
    name = models.CharField(max_length=100, )

    def __str__(self):
        return self.name


class LessonDevelopments(models.Model):
    lesson_topic = models.CharField(max_length=50, verbose_name='Dars mavzusi')
    lesson_desc = models.CharField(max_length=255, verbose_name='Dars haqida qisqacha')
    lesson_date = models.DateField(verbose_name='Darsnig boshlanish vaqti')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Staff(models.Model):
    staff = models.CharField(max_length=50)

    class Meta:
        db_table = 'staff'


class TradeUnion(models.Model):
    trade_union_name = models.CharField(max_length=100, verbose_name='Kasaba uyishmasi nomi')
    trade_union_leader = models.CharField(max_length=50, verbose_name='Kasaba uyishmasi rahbari')
    trade_union_desc = models.CharField(max_length=255, verbose_name='Kasaba uyishmasi haqida qisqacha')
    trade_union_staff = models.ManyToManyField(Staff)

    def __str__(self):
        return self.trade_union_name

    class Meta:
        db_table = 'trade_union'