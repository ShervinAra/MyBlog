#coding:    utf8
import datetime

from django.http import  HttpResponse    ,   Http404 ,   HttpResponseRedirect
from django.shortcuts    import  render_to_response  as  rr
from django.contrib.auth.models  import  User
from django.contrib.auth import  authenticate,   login
from django.template import  RequestContext
from django.contrib.auth.decorators import login_required

from MyBlog.data.models  import  context
from MyBlog.data.models  import  comment
from MyBlog.forms    import  AuthForm


now = datetime.datetime.now()

@login_required
def user_homepage(request,user):
    contexts = context.user_post(request.user)
    return  rr('home.html',
               {'now':now,
                'contexts':contexts,
                'user':user},
                context_instance=RequestContext(request))
