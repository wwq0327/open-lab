#! -*- coding: utf-8 -*-

import markdown
from django.db import models
from django.contrib.auth.models import User
from tagging.fields import TagField
from tagging.models import Tag

from utils import get_partition_id, safe_filename
from storage import ImageStorage

def determine_image_upload_path(instance, filename):
    return "uploads/%(filename)s" % {
        'filename': safe_filename(filename),
        }

class Projects(models.Model):
    title = models.CharField(u'项目标题', max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    tags = TagField(u'标签', blank=True, help_text=u'加一个适合的标签以便你能更方便的对项目进行分类，标签之间请用空格分隔')
    creater = models.ForeignKey(User)
    image = models.ImageField(u'项目图片',
                              upload_to=determine_image_upload_path,
                              storage=ImageStorage(),
                              #blank=True,
                              #null=True,
                              help_text=u'给项目一个图片，可增加你项目的关注度')
    description = models.TextField(u'项目描述', blank=True, null=True,
                                help_text=u'给项目一个简单的描述')
    description_html = models.TextField(editable=False)
    content = models.TextField(u'项目内容',
                          help_text=u'项目是什么，怎么做')
    content_html = models.TextField(editable=False)
    video = models.URLField(u'视频链接', max_length=255,
                            blank=True,
                            null=True,
                            help_text=u'你可以为你的项止录制一个关于创意的视频或课程实施的视频')
    #follower = models.ForeignKey(PrjFollower)

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return 'Projects %s:%s' % (self.pk, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('prj_page', (), {
            'prj_pk': self.pk
            })

    def _get_tags(self):
        return Tag.objects.get_for_object(self)

    def _set_tags(self, tags):
        return Tag.objects.update_tags(self, tags)

    obj_tags = property(_get_tags, _set_tags)

    def save(self, *args, **kwargs):
        self.description_html = markdown.markdown(self.description)
        self.content_html = markdown.markdown(self.content)
        super(Projects, self).save(*args, **kwargs)


class PrjFollower(models.Model):
    create_on = models.DateTimeField(auto_now_add=True)
    creater = models.ForeignKey(User)
    project = models.ForeignKey(Projects)

    class Mate:
        ordering = ['-id']

    def __unicode__(self):
        return 'PrjFollower %s:%s' % (self.creater.username,
                                      self.project.title)




