# -*- coding:utf-8 -*-
__author__ = 'pizi'
__data__ = '2017/10/9 18:28'

from django.conf.urls import url, include

from .views import CourseListView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$',CourseListView.as_view(), name= "course_list"),


]