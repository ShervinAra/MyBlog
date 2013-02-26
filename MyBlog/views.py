from django.http import HttpResponse , Http404 , HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from MyBlog.data.models import context as ct
from MyBlog.data.models import comment as cm
from MyBlog.forms import auth_form


import datetime
now=datetime.datetime.now()


def homepage(request):
	form = auth_form()
	return render_to_response('index.html', {'form':form,})


def auth(request):	
	errors= []
	if request.method == 'GET' and 'user' and 'password' in request.GET:
		if not request.GET.get('user','') and not request.GET.get('password',''):
			errors.append('Enter username  and password.')
			return HttpResponseRedirect('/')
		elif not request.GET.get('password',''):
			errors.append('Enter password.')
			return HttpResponseRedirect("/")
			return render_to_response('index.html', {'errors' : errors})
		elif not request.GET.get('user',''):
			errors.append('Enter user.')
			return HttpResponseRedirect("../")
			return render_to_response('index.html', {'errors' : errors})		
		if request.GET['user'] and request.GET['password']:
			user = request.GET['user']
			password = request.GET['password']
		else:
			errors.append('Your request invalid.')
			return render_to_response('index.html', {'errors' : errors})
		if user == "shervin" and password == "shit":		
			return HttpResponseRedirect("/home/%s/" %(user))
			
		else:
			errors.append('Authentication failure')
			return render_to_response('index.html', {'errors' : errors})
	else:
		errors.append('Your request invalid.')
		return render_to_response('index.html', {'errors' : errors})		


def register(request):
	pass
	

def user_homepage(request,user):	
	c=ct.objects.all()
	cn=cm.objects.all()
	return render_to_response('home.html',
		{'now':now,
		'post':c,
		'comment':cn,
		'user':user},
	context_instance=RequestContext(request))

	
def about(request):
	return render_to_response('about.html',{'now':now,})
