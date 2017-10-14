# -*- coding:utf-8 -*-
__author__ = 'pizi'
__data__ = '2017/10/12 23:35'


from django.conf.urls import url, include
from .views import UserInfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView
from .views import MyCourseView, MyfavOrgView, MyfavTeacherView, MyfavCourseView, MymessageView
urlpatterns = [
    # 用户信息
    url(r'^info/$',UserInfoView.as_view(), name= "user_info"),

    # 用户上传头像
    url(r'^image/upload/$',UploadImageView.as_view(), name= "image_upload"),

     # 用户修改密码
    url(r'^update/pwd/$',UpdatePwdView.as_view(), name= "update_pwd"),

     # 发送邮箱验证码
    url(r'^sendemail_code/$',SendEmailCodeView.as_view(), name= "sendemail_code"),

    # 修改邮箱
    url(r'^update_email/$',UpdateEmailView.as_view(), name= "update_email"),

    # 修改邮箱
    url(r'^mycourse/$',MyCourseView.as_view(), name= "mycourse"),

    # 收藏机构
    url(r'^myfav/org/$',MyfavOrgView.as_view(), name= "myfav_org"),

    # 收藏老师
    url(r'^myfav/teacher/$',MyfavTeacherView.as_view(), name= "myfav_tescher"),

    # 收藏机构
    url(r'^myfav/course/$',MyfavCourseView.as_view(), name= "myfav_course"),

    # 我的消息
    url(r'^mymessage/$',MymessageView.as_view(), name= "mymessage"),

]