from django.contrib import admin
from blog_app.models import BlogRecord


# Register your models here.
@admin.register(BlogRecord)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'published', 'viewed',)
    list_filter = ('title', )
    search_fields = ('title',)
