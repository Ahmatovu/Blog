from django.contrib import admin
from .models import Post, Author, Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags','date',) # fields in models.py in post class
    list_display = ('title','date','author',)
    prepopulated_fields = {'slug': ('title',)} #automatically displays title on slug

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'post')

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
