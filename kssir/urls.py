"""
Definition of urls for kssir.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()
from shoortner.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', kssir.views.home, name='home'),
    # url(r'^kssir/', include('kssir.kssir.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^(?P<shortcode>[\w-]+){6,15}/$',kssir_redirect_view, name="kssirfbv"),
    url(r'^(?P<shortcode>[\w]+)/$',URLRedirectView.as_view(), name="kssircbv"),
    url(r'^$', HomeView.as_view(),name="index"),
]
