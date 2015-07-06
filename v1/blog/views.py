from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Blog, Topic, Tag
# Create your views here.
def blogs(request):
    return render_to_response('blogs.html', {
        'topics': Topic.objects.all(),
        'blogs': Blog.objects.all()[:5]
    })
	
def view_blog(request, slug):
    print(slug)
    return render_to_response('blog.html', {
        'blog': get_object_or_404(Blog, slug=slug)
    })
	
def view_topic(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    return render_to_response('view_topic.html', {
        'topic': topic,
        'blogs': Blog.objects.filter(topic=topic)[:5]
    })
	
def view_tag(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    return render_to_response('view_tag.html', {
        'tag': tag,
        'blogs': Blog.objects.filter(tag=tag)[:5]
    })