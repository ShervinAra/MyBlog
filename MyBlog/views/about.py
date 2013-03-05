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

def about(request):
	return rr('about.html',{'now':now,})
