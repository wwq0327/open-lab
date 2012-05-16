#! -*- coding: utf-8 -*-

from django import forms
from bootstrap.forms import BootstrapModelForm
from projects.models import Projects

from django.conf import settings

class ProjectsForm(BootstrapModelForm):
    class Meta:
        model = Projects
        fields = ('title', 'image', 'video', 'description', 'content', 'tags', )

    def clean_image(self):
        if self.cleaned_data['image'].size > settings.MAX_IMAGE_SIZE:
            max_size = settings.MAX_IMAGE_SIZE / 1024
            ms = ''

        return self.cleaned_data['image']

    ## def save(self, force_insert=False, force_update=False, commit=True):
    ##     project = super(ProjectsForm, self).save(commint=commint)
    ##     #user = project.user
    ##     project.image = self.clean_image()
    ##     project.save()

    ##     return project

        def save(self):
            model = Projects(title=self.cleaned_data['title'],
                             image=self.cleaned_data['image'],
                             video=self.cleaned_data['video'],
                             description=self.cleaned_data['descript'],
                             content=self.cleaned_data['content'],
                             tags=self.cleaned_data['tags'],
                             #creater=user
                             )
            model.save()

            return model

