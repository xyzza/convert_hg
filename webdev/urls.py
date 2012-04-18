#coding:utf-8
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

# Автоматическое распознование администарторских модулей
# должно происходить до регистрации urlpatterns
admin.autodiscover()

# Регистрация ссылок
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webdev.views.home', name='home'),
    # url(r'^webdev/', include('webdev.foo.urls')),
    # doc
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # урл админской
    url(r'^admin/', include(admin.site.urls)),
)