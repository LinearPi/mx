# -*- coding:utf-8 -*-
__author__ = 'pizi'
__data__ = '2017/10/12 23:35'


from django.conf.urls import url, include
from .views import UserInfoView, UpLoadView

urlpatterns = [
    # 用户信息
    url(r'^info/$',UserInfoView.as_view(), name= "user_info"),

    # 用户上传头像
    url(r'^image/upload/$',UpLoadView.as_view(), name= "image_upload"),

]