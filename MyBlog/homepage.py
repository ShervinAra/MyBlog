def homepage(request):
	if request.method == "POST":
		form = AuthForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			
			user = authenticate(username=username, password=password)
			if user:
				login(request, user)
				return HttpResponseRedirect("/home/%s" % user.username)
			else:
				return rr("index.html", {'errors': "Invalid username or password",
											'form': form},
					context_instance=RequestContext(request))

		return rr('index.html', {"form": form},
				context_instance=RequestContext(request))
	else:
		form = AuthForm()
		return rr('index.html', {'form':form},
					context_instance=RequestContext(request))
