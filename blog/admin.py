from django.contrib import admin
from .models import Post, Comment, Contact, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'is_published')
    search_fields = ('title', 'description')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post', 'created_at')

admin.site.register(Post),
admin.site.register(Comment)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'is_solved')


admin.site.register(Contact)
admin.site.register(Category)
