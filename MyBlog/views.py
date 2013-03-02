import datetime

from django.http import HttpResponse , Http404 , HttpResponseRedirect
from django.shortcuts import render_to_response as rr
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext

from MyBlog.data.models import context
from MyBlog.data.models import comment
from MyBlog.forms import auth_form


now = datetime.datetime.now()


def homepage(request):
	form = auth_form()
	return rr('index.html', {'form':form,})


def auth(request):
	return HttpResponse(request.method)
	if request.method == "POST":
		if "login" in request.POST:
			if request.POST["login"] == "Login":
				return login_view(request)
			elif request.POST["register"] == "Register":
				return register_view(request)
			else:
				return rr('index.html',
					  {"errors": "Use a submit button."},
					  context_instance=RequestContext(request))
	else:
		return rr('index.html')


def login_view(request):
	username = request.POST.get("username", None)
	password = request.POST.get("password", None)

	if not username or not password:
		return rr("index.html", {'errors': "Invalid username or password"},
			  context_instance=RequestContext(request))
	user = authenticate(username=username, password=password)
	if user:
		login(request, user)
		return HttpResponseRedirect("/home/%s" % username.username)
	else:
		return rr("index.html", {'errors': "Invalid username or password"},
			  context_instance=RequestContext(request))


def register_view(request):
	pass
	
	

def user_homepage(request,user):	
	contexts = context.objects.all()
	comments = comment.objects.all()
	return rr('home.html',
		{'now':now,
		'contexts':contexts,
		'comments':comments,
		'user':user},
	context_instance=RequestContext(request))

	
def about(request):
	return rr('about.html',{'now':now,})
