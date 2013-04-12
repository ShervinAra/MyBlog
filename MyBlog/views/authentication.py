#coding: utf8
import datetime

from django.http import HttpResponse , Http404 , HttpResponseRedirect
from django.shortcuts import render_to_response as rr
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.template import RequestContext

from MyBlog.data.models import context
from MyBlog.data.models import comment
from MyBlog.forms import AuthForm

def homepage(request):
	if request.method == "POST":
		form = AuthForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				return HttpResponseRedirect("/users/%s" % user.username)
			else:
				return rr("index.html", {'errors': "Invalid username or password",
											'form': form},
					context_instance=RequestContext(request))

		#return rr('index.html', {"form": form},
				#context_instance=RequestContext(request))
	else:
		form = AuthForm()
		return rr('index.html', {'form':form},
					context_instance=RequestContext(request))
