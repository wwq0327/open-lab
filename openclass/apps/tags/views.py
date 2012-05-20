#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.models import User

from tagging.models import Tag, TaggedItem
from tagging.utils import calculate_cloud, LOGARITHMIC

from projects.models import Projects, top_comments

def all_tags(request):
    clouds = Tag.objects.cloud_for_model(Projects,
                                         steps=settings.TAG_LIST_LEVEL,
                                         distribution=LOGARITHMIC,
                                         filters=None,
                                         min_count=None)
    return render_to_response('tags/all_tags.html',
                              {
                                  'clouds': clouds,
                                  },
                              context_instance=RequestContext(request))


def prj_tag(request, tag):
    '''相应tag的所有项目列表'''

    o = get_object_or_404(Tag, name=tag)
    prjs = TaggedItem.objects.get_by_model(Projects, o)
    new_prj = Projects.objects.all()[:10]

    return render_to_response('projects/index.html',
                              {
                                  'prjs': prjs,
                                  'top_comments': top_comments(),
                                  'new_prj': new_prj,
                                  'tag': tag,
                                  },
                              context_instance=RequestContext(request))


def prj_user_tag(request, tag, username):
    '''相应tag的所有项目列表'''

    is_user_tag = True
    o = get_object_or_404(Tag, name=tag)
    u = get_object_or_404(User, username=username)

    ps = TaggedItem.objects.get_by_model(Projects, o)

    prjs = [p for p in ps if p.creater==u]

    new_prj = Projects.objects.all()[:10]

    return render_to_response('projects/index.html',
                              {
                                  'prjs': prjs,
                                  'top_comments': top_comments(),
                                  'new_prj': new_prj,
                                  'tag': tag,
                                  'is_user_tag': is_user_tag,
                                  'c_user': username,
                                  },
                              context_instance=RequestContext(request))


