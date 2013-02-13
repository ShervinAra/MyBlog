from django.conf.urls.defaults import *
from MyBlog.views import *

import os
from django.conf.urls import *
from django.contrib import admin
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^MyBlog/', include('MyBlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    ('^$' , homepage),
    
)

# Local media serving.
if settings.DEBUG:
    urlpatterns += patterns('',
            (r'^statics/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': os.path.join(os.path.dirname(__file__),\
                                    '../statics').replace('\\', '/')}),
)