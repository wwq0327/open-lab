# -*- coding: utf-8 -*-
from django import forms
#from django.utils.translation import ugettext_lazy as _

from userena.forms import SignupForm, AuthenticationForm
#from bootstrap.forms import BootstrapMixin

USERNAME_RE = r'^\S+$'
attrs_dict = {'class': 'required'}

class BsSignupForm(SignupForm):
#lass BsSignupForm(SignupForm, BootstrapMixin):
    username = forms.RegexField(regex=USERNAME_RE,
                                max_length=30,
                                widget=forms.TextInput(attrs=attrs_dict),
                                label=u"用户名",
                                error_messages={'invalid': u'Username must contain only letters, numbers, dots and underscores.'})

    def __init__(self, *args, **kw):
        super(BsSignupForm, self).__init__(*args, **kw)
        #self.__bootstrap__()

class BsAuthenticationForm(AuthenticationForm):
#class BsAuthenticationForm(AuthenticationForm, BootstrapMixin):

    def __init__(self, *args, **kw):
        super(BsAuthenticationForm, self).__init__(*args, **kw)
        #self.__bootstrap__()
