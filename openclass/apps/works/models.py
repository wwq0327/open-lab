#! -*- coding: utf-8 -*-

import datetime
import markdown

from django.db import models
from django.contrib.auth.models import User

from tagging.fields import TagField
from tagging.models import Tag

class Works(models.Model):
    title = models.CharField(u'题目', max_length=255)
    content = models.TextField(u'内容')
    content_html = models.TextField(editable=False)
    creater = models.ForeignKey(User)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date =  models.DateTimeField(auto_now=True)
    tags = TagField(u'标签', blank=True, help_text=u"标签间请用空格分隔")

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return "Works %s" % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('ws_page', (), {
            'ws_pk': self.pk
            })

    def save(self, *args, **kwargs):
        self.content_html = markdown.markdown(self.content)
        super(Works, self).save(*args, **kwargs)

    def _get_tags(self):
        return Tag.objects.get_for_object(self)

    def _set_tags(self, tags):
        return Tag.objects.update_tags(self, tags)

    obj_tags = property(_get_tags, _set_tags)
