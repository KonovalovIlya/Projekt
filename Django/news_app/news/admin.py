from django.contrib import admin
from news.models import News, Comment
# Register your models here.


class CommentInLine(admin.StackedInline):
    model = Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at', 'interest']
    list_filter = ['interest']
    inlines = [CommentInLine]

    actions = ['mark_as_true', 'mark_as_false']

    def mark_as_true(self, request, queryset):
        queryset.update(interest=True)

    def mark_as_false(self, request, queryset):
        queryset.update(interest=False)

    mark_as_true.short_description = 'Перевести в статус Активна'
    mark_as_false.short_description = 'Перевести в статус Не активна'


# @admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'comment', 'news']
    list_filter = ['user']

    actions = ['delete',]

    def delete(self, request, queryset):
        queryset.update(comment='Удалено администратором')

    delete.short_description = 'Удалить содержание комментария'

    # exclude = ('user',)  # скрыть author поле, чтобы оно не отображалось в форме изменений
    #
    # def save_model(self, request, obj, form, change):
    #     if not obj.pk:
    #         obj.user = request.user
    #     super().save_model(request, obj, form, change)


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
