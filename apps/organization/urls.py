# -*- coding:utf-8 -*-
__author__ = 'pizi'
__data__ = '2017/10/6 9:03'

from django.conf.urls import url, include

from .views import OrgView, AddUserAskView, OrgHomeVies


urlpatterns = [
    url(r'^list/$',OrgView.as_view(), name= "org_list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name= "add_ask"),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeVies.as_view(), name= "org_home"),

]