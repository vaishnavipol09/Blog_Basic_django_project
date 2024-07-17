from django.contrib import admin # type: ignore

from .models import Post, Author, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tags', 'date')
    list_display = ('title', 'date', 'author')

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
