import os
from MyBlog.views import *
from django.conf.urls import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyBlog.views.home', name='home'),
    # url(r'^MyBlog/', include('MyBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #(r'^admin/', include(admin.site.urls)),
    (r'^$' , "MyBlog.views.homepage"),
    (r'^authentication/$' , "MyBlog.views.auth"),
    (r'^register/$' , "MyBlog.views.register"),
    (r'^home/(\w*)/$' , "MyBlog.views.user_homepage"),
    (r'^about/$' , "MyBlog.views.about"),
    (r'^comments/', include('django.contrib.comments.urls')),
)
# Local media serving.
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^statics/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': os.path.join(os.path.dirname(__file__),\
                                    '../statics').replace('\\', '/')}),
)
