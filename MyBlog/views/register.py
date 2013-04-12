#coding: utf8
import datetime

from django.http import HttpResponse , Http404 , HttpResponseRedirect
from django.shortcuts import render_to_response as rr
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template import RequestContext

from MyBlog.data.models import context, comment
from MyBlog.forms import AuthForm
from MyBlog.forms import RegisterForm


now = datetime.datetime.now()


def register_view(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			password_confirm = form.cleaned_data["password_confirm"]
			first_name = form.cleaned_data["first_name"]
			last_name = form.cleaned_data["last_name"]
			email = form.cleaned_data["email"]	
		return rr('index.html', {"form": form},
			context_instance=RequestContext(request))
	else:
		form = RegisterForm()
		return rr('register.html', {'form':form},
			  context_instance=RequestContext(request))
