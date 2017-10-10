# -*- coding:utf-8 -*-
__author__ = 'pizi'
__data__ = '2017/10/9 18:28'

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentView

urlpatterns = [
    # 课程机构列表页
    url(r'^list/$',CourseListView.as_view(), name= "course_list"),

    # 课程详情表页
    url(r'^detail/(?P<course_id>\d+)/$',CourseDetailView.as_view(), name= "course_detail"),

    # 课程视频表页
    url(r'^info/(?P<course_id>\d+)/$',CourseInfoView.as_view(), name= "course_info"),

    # 课程评论表页
    url(r'^comment/(?P<course_id>\d+)/$',CommentsView.as_view(), name= "course_comments"),

    # 添加评论信息
    url(r'^add_comment/$',AddCommentView.as_view(), name= "add_comment"),


]