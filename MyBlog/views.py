from django.http import HttpResponse , Http404
from django.shortcuts import render_to_response
from MyBlog.data.models import context as ct
from MyBlog.data.models import comment as cm
from django.template import RequestContext

import datetime


now=datetime.datetime.now()

def homepage(request):	
	c=ct.objects.all()
	cn=cm.objects.all()
	return render_to_response('index.html',
		{'now':now,
		'post':c,
		'comment':cn,},
	context_instance=RequestContext(request))

	
def about(request):
	return render_to_response('about.html',{'now':now,})


def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		post = ct.objects.filter(Subject__icontains=q)		
		return render_to_response('index.html',{'post':post , 'query':q})
	else:
		return render_to_response('index.html', {'error':True} )		


def test(request):
	return HttpResponse(request.META['REMOTE_ADDR'])
