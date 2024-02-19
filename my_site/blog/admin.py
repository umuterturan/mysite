from django.contrib import admin

from .models import Post, Author, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date")
    list_display = ("title", "date", "author")
    prepopulated_fields = {"slug" : ("title",)}

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('first_name', 'last_name',)}        


admin.site.register(Author,AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)


