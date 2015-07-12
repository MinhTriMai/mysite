from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from blog.models import Blog, Topic, Tag
from django.core.paginator import Paginator, EmptyPage
# Create your views here.
def blogs(request, selected_page=1):
    # Get all blog posts
    blogs = Blog.objects.all().filter(hiden=False).order_by('date')
    # Add pagination
    pages = Paginator(blogs, 3)
    # Get the specified page
    try:
        returned_page = pages.page(selected_page)
    except EmptyPage:
        returned_page = pages.page(pages.num_pages)
	
    return render_to_response('blogs.html', {
        'topics': Topic.objects.all().order_by('name'),
		'tags': Tag.objects.all().order_by('name'),
        'blogs': returned_page.object_list,
        'page': returned_page
    })
	
def view_blog(request, slug):
    print(slug)
    return render_to_response('blog.html', {
        'topics': Topic.objects.all().order_by('name'),
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
    return render_to_response('view_tag.html', {
        'tag': tag,
        'blogs': Blog.objects.filter(tag=tag)[:5]
    })