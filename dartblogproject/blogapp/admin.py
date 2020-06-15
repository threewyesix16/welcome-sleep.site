from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Tag, Post, Comment


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    save_on_top = True
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'category', 'author', 'created_at', 'views', 'photo', 'miniature',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content',)
    list_filter = ('category',)
    fields = ('id', 'title', 'slug', 'category', 'tags', 'content', 'author', 'photo', 'miniature', 'created_at', 'views',)
    readonly_fields = ('id', 'created_at', 'views', 'miniature',)

    def miniature(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" height=50>')
        else:
            return '-'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author_name', 'post', 'created_at', )
    list_display_links = ('id', 'author_name', )
    list_filter = ('author_name', 'post', )



admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
