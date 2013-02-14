from django.http import HttpResponse , Http404
from django.shortcuts import render_to_response
from MyBlog.data.models import *


import datetime
now=datetime.datetime.now()

def homepage(request):	
	return render_to_response('index.html',{'now':now,})
	
def about(request):
	return render_to_response('about.html',{'now':now,})

def post(request):
	c=context.objects.all()
	#name=c.Name
	#post=c.Post
	return render_to_response('index.html', {'post':c,})	
		
