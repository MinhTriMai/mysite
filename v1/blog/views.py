from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Blog, Topic, Tag
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
# Create your views here.
def blogs(request, selected_page=1):
    # Get all blog posts
    topic_project = get_object_or_404(Topic, name='Project')
    blogs = Blog.objects.all().filter(hiden=False).exclude(topic=topic_project).order_by('-date')
    featured_blogs = Blog.objects.all().filter(hiden=False, featured=True).exclude(topic=topic_project).order_by('-date')
    
    # Add pagination
    pages = Paginator(blogs, 5)
    # Get the specified page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)
	
    return render_to_response('blogs.html', {
        'topics': Topic.objects.all().exclude(name='Project').order_by('name'),
		'tags': Tag.objects.all().order_by('name'),
        'blogs': returned_page.object_list,
        'page': returned_page,
		'featured_blogs': featured_blogs
    })
	
def view_blog(request, slug):
    return render_to_response('blog.html', {
        'topics': Topic.objects.all().exclude(name='Project').order_by('name'),
		'tags': Tag.objects.all().order_by('name'),
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
    topic_project = get_object_or_404(Topic, name='Project')
    return render_to_response('blogs.html', {
        'tag': tag,
        'topics': Topic.objects.all().exclude(name='Project').order_by('name'),
		'tags': Tag.objects.all().order_by('name'),
        'blogs': Blog.objects.all().filter(tag=tag, hiden=False).exclude(topic=topic_project).order_by('-date'),
    })
	
def projects(request):
    # Get all project posts
    topic_project = get_object_or_404(Topic, name='Project')
    projects = Blog.objects.all().filter(hiden=False, topic=topic_project).order_by('-date')
    	
    return render_to_response('projects.html', {
        'projects': projects,
    })
	
def view_project(request, slug):
    return render_to_response('project.html', {
        'project': get_object_or_404(Blog, slug=slug)
    })