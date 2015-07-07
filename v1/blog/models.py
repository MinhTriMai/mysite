from django.db import models
from django.db.models import permalink

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    date = models.DateField(db_index=True, auto_now_add=True)
    topic = models.ForeignKey('blog.Topic')
    tag = models.ManyToManyField('blog.Tag', blank=True)
    image = models.ImageField(upload_to="user_upload/images/", blank=True)
    file = models.FileField(upload_to="user_upload/files/", blank=True)
	
    def __str__(seft):
        return seft.title    
		
    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })
		
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