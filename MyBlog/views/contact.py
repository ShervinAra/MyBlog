#coding: utf8
import datetime

from django.http import HttpResponse , Http404 , HttpResponseRedirect
from django.shortcuts import render_to_response as rr
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.template import RequestContext

from MyBlog.data.models import context
from MyBlog.data.models import comment
from MyBlog.forms import AuthForm
from MyBlog.forms import RegisterForm


now = datetime.datetime.now()


def contact_view(request):
	return rr('contact.html')
