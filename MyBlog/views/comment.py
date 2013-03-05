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


now = datetime.datetime.now()

def comment_view(request):
	if request.method == "POST":
		if "send" in request.POST:
			name = request.POST.get("name", None)
			content = request.POST.get("content", None)
			if not name or not comment:
				return rr("home.html", {'errors': "Invalid username or password"})			
			else:
				cm = MyBlog.data.comment
				cm.Name = name
				cm.Content = content	
				cm.save()
