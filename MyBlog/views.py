from django.http import HttpResponse , Http404
from django.shortcuts import render_to_response


def homepage(request):
	import datetime
	now=datetime.datetime.now()
	return render_to_response('index.html',{'now':now,})
