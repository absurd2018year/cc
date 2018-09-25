
from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):
    """
    校验登录信息
    """
    username = forms.CharField(max_length=6, min_length=2,
                               error_messages={
                                   'max_length': '用户名不能超过6个字符',
                                   'min_length': '用户名不能低于2个字符'
                               })
    userpwd = forms.CharField(min_length=6,
                              error_messages={
                                  'min_length': '密码不能少于6个字符'
                              })

    def clean(self):
        """
        校验用户名
        """
        user = User.objects.filter(username=self.cleaned_data['username'])

        if not user:
            if not user:
                raise forms.ValidationError({'username': '请先注册再来登录'})
            return self.cleaned_data
