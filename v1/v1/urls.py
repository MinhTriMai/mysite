"""v1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'blog.views.default'),
	url(r'^about/$', TemplateView.as_view(template_name='about.html')),
	url(r'^contact/$', 'form.views.contact'),
    url(r'^thank-you/$', TemplateView.as_view(template_name='thank-you.html')),
	url(r'^blogs/$', 'blog.views.blogs'),
	url(r'^blogs/(?P<selected_page>\d+)/?$', 'blog.views.blogs'),
    url(
        r'^blog/view/(?P<slug>[^\.]+).html', 
        'blog.views.view_blog', 
        name='view_blog_post'),
    url(r'^projects/$', 'blog.views.projects'),
    url(
        r'^project/view/(?P<slug>[^\.]+).html', 
        'blog.views.view_project', 
        name='view_project_post'),
    url(
        r'^blog/topic/(?P<slug>[^\.]+).html', 
        'blog.views.view_topic', 
        name='view_blog_topic'),
	url(
        r'^blog/tag/(?P<slug>[^\.]+).html', 
        'blog.views.view_tag', 
        name='view_blog_tag'),
	url(r'^search/$', 'blog.views.search'),
]
