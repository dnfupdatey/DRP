from django.conf.urls import patterns, include, url
from django.contrib import admin
import public
import authentication
import database

admin.autodiscover()

urlpatterns = patterns('',
  (r'^', include(public.urls)),
  (r'^', include(authentication.urls)),
  (r'^database/', include(database.urls)),
  (r'^admin/', include(admin.site.urls))
)