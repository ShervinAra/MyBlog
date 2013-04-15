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
		if "name" in request.POST and "content" in request.POST:
			return HttpResponse("ok")
			name = request.POST.get("name", None)
			content = request.POST.get("content", None)
			if not name or not comment:
				return rr("home.html", {'errors': "Fields are empty"})			
			else:
				cm = comment
				cm.Name = name
				cm.Content = content	
				cm.save()
				return HttpResponse("ok")


def edit_comment(request):
	return HttpResponse("ok")
	
def delete_comment(request):
	return HttpResponse("ok")	
