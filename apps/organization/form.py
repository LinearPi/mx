# -*- coding:utf-8 -*-
__author__ = 'pizi'
__data__ = '2017/10/5 22:31'

import re
from django import forms

from operation.models import UserAsk

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        PEGEX_MOBILE =  "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(PEGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u"手机号码非法", code= "mobile_invalid")

