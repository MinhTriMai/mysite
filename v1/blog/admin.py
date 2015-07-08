from django.contrib import admin
from blog.models import Blog, Topic, Tag, BlogImage, BlogFile
from django.template.defaultfilters import slugify

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    exclude = ['date']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'topic', 'date')
    search_fields = ['title']

class TopicAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
	
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(BlogImage)
admin.site.register(BlogFile)