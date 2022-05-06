from django.contrib import admin
from news.models import News, Comment


class CommentInLine(admin.StackedInline):
    model = Comment


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'updated_at', 'interest']
    list_filter = ['interest']
    inlines = [CommentInLine]

    actions = ['mark_as_true', 'mark_as_false']

    def mark_as_true(self, request, queryset):
        queryset.update(interest=True)

    def mark_as_false(self, request, queryset):
        queryset.update(interest=False)

    mark_as_true.short_description = 'Перевести в статус Активна'
    mark_as_false.short_description = 'Перевести в статус Не активна'


class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'anonusername', 'comment', 'news']
    list_filter = ['user', 'anonusername']

    actions = ['delete']

    def delete(self, request, queryset):
        queryset.update(comment='Удалено администратором')

    delete.short_description = 'Удалить содержание комментария'


admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)
