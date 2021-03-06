from django.contrib import admin

from .models import Post

class PostAdmin(admin.ModelAdmin):
        list_display = ('title', 'autor', 'created_date', 'published_date')
        list_filter = ('created_date', 'autor', 'published_date')


admin.site.register(Post, PostAdmin)
