# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from rome_app import views
from django.contrib import admin


urlpatterns = patterns('',
    #admin
    url(r'^admin/', include(admin.site.urls), name='admin'),

    #index and static
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^links/$', views.links, name='links'),

    #books, prints, and essays
    url(r'^books/$', views.book_list, name='books'),
    url(r'^books/(?P<book_pid>\d+)/$', views.book_detail, name='thumbnail_viewer'),
    url(r'^books/(?P<book_pid>\d+)/(?P<page_pid>\d+)/$', views.page_detail, name='book_page_viewer'),
    url(r'^pages/(?P<page_pid>\d+)/$', views.page_detail, name='page_viewer'),
    url(r'^pages/$', views.book_list, name='page_back_link'),
    url(r'^prints/$', views.print_list, name='prints'),
    url(r'^prints/(?P<print_pid>\d+)/$', views.print_detail, name='specific_print'),
    url(r'^essays/$', views.essay_list, name='essays'),
    url(r'^essays/(?P<essay_slug>\w+)/$', views.essay_detail, name='specific_essay'),
    url(r'^people/$', views.biography_list, name='people'),
    url(r'^people/(?P<trp_id>\d+)/$', views.biography_detail, name='person_detail'),
    url(r'^people/(?P<trp_id>\d+)/TEI/$', views.person_detail_tei, name='person_detail_tei'),
)
