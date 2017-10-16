# -*- coding:utf-8 -*-
__author__ = 'pizi'
__data__ = '2017/10/1 23:25'

import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'city', 'category', 'add_time']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'category', 'city']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'city', 'category', 'add_time']
    relfield_style = 'fk-ajax'


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['name', 'org', 'work_years', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['name', 'org', 'work_years', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)