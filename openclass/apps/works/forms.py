#! -*- coding: utf-8 -*-

from django import forms
from bootstrap.forms import BootstrapModelForm
from works.models import Works

#class WorksForm(forms.ModelForm):
class WorksForm(BootstrapModelForm):
    class Meta:
        model = Works
        fields = ('title', 'content', 'tags', )

    def save(self, user):
        model = Works(
            title=self.cleaned_data['title'],
            content = self.cleaned_data['content'],
            tags = self.cleaned_data['tags'],
            creater = user)
        model.save()

        return model

