from django.http import HttpResponse , Http404
from django.shortcuts import render_to_response
from MyBlog.data.models import context as ct
from django.template import RequestContext

import datetime


now=datetime.datetime.now()

def homepage(request):	
	c=ct.objects.all()
	return render_to_response('index.html',
		{'now':now,
		'post':c,},
	context_instance=RequestContext(request))

	
def about(request):
	return render_to_response('about.html',{'now':now,})
	
		
