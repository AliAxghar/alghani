from django.contrib import admin
from .models import Post_blog
# Register your models here.

class Post_blogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category','created_on')
    list_filter = ("category",)
    search_fields = ['title', 'para1']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post_blog, Post_blogAdmin)
