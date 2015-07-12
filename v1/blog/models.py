from django.db import models
from django.db.models import permalink

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField(default='', blank=True)
    description = models.TextField(default='', blank=True)
    date = models.DateField(db_index=True, auto_now_add=True)
    topic = models.ForeignKey('blog.Topic')
    tag = models.ManyToManyField('blog.Tag', blank=True)
    images = models.ManyToManyField('blog.BlogImage', blank=True)
    files = models.ManyToManyField('blog.BlogFile', blank=True)
    hiden = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    isProject = models.BooleanField(default=False)
	
    def __str__(seft):
        return seft.title
		
    @permalink
    def get_absolute_url(self):
	    if (self.isProject == True):
		    return ('view_project_post', None, { 'slug': self.slug })
	    else:
		    return ('view_blog_post', None, { 'slug': self.slug })
		
class BlogImage(models.Model):
    image = models.ImageField(upload_to="static/user_upload/images/")
	
    def __str__(seft):
        return seft.image.url
	
class BlogFile(models.Model):
    file = models.FileField(upload_to="static/user_upload/files/")
	
    def __str__(seft):
        return seft.file.url
		
class Topic(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(db_index=True)
    description = models.TextField(max_length=500, blank=True)
	
    def __str__(seft):
        return seft.name	

    @permalink
    def get_absolute_url(self):
        return ('view_blog_topic', None, { 'slug': self.slug })
		
class Tag(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(db_index=True)
    description = models.TextField(max_length=500, blank=True)
	
    def __str__(seft):
        return seft.name

    @permalink
    def get_absolute_url(self):
        return ('view_blog_tag', None, { 'slug': self.slug })