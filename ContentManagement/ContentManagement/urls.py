from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$','articles.views.home_page'),
     url(r'^ContentManagement/$','articles.views.home'),
     url(r'^ContentManagement/(?P<article_id>\d+)/$','articles.views.home'),
    # url(r'^ContentManagement/', include('ContentManagement.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
