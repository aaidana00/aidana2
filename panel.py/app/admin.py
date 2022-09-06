from django.contrib import admin
from .models import News
from django.utils.safestring import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = News
        fields = '__all__'


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'content', 'created', 'updated', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_filter = ('is_published', 'created')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width=250')
        else:
            return '-'


