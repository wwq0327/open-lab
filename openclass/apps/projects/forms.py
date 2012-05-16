#! -*- coding: utf-8 -*-

from django import forms
from bootstrap.forms import BootstrapModelForm
from projects.models import Projects

class ProjectsForm(BootstrapModelForm):
    class Meta:
        model = Projects
        fields = ('title', 'image', 'video', 'describe', 'content',)

