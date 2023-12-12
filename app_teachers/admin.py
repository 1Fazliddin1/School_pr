from django.contrib import admin

from .models import Teachers, LessonDevelopments, TradeUnion, Staff, Category

admin.site.register(Staff)
admin.site.register(Category)


@admin.register(TradeUnion)
class TradeUnionAdmin(admin.ModelAdmin):
    fields = ['trade_union_name', 'trade_union_leader', 'trade_union_desc', 'trade_union_staff']
    list_display = ['id', 'trade_union_name', 'trade_union_leader', 'trade_union_desc']
    search_fields = ['trade_union_desc', 'trade_union_staff']


@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    fields = ['teach_first_name', 'teach_last_name', 'teach_informations', 'teach_specialist']
    list_display = ['id', 'teach_first_name', 'teach_specialist']
    search_fields = ['teach_first_name', 'teach_last_name', 'teach_informations']


@admin.register(LessonDevelopments)
class LessonDevelopmentsAdmin(admin.ModelAdmin):
    fields = ['lesson_topic', 'lesson_desc', 'lesson_date', 'category']
    list_display = ['id','lesson_topic','lesson_desc', 'lesson_date',]
    search_fields = ['lesson_desc', 'category']
