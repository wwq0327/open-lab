#! -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from works.models import Works
from works.forms import WorksFormb

def index(request):
    works = Works.objects.all()
    return render_to_response('works/index.html',
                              {
                                  'works': works,
                                  },
                              context_instance=RequestContext(request))

@login_required
def ws_create(request):
    '''创建作品'''

    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            model = form.save(commit=False)
            model.creater = request.user
            model.save()
            return HttpResponseRedirect(model.get_absolute_url())
    else:
        form = WorksForm()

    return render_to_response('works/ws_create.html',
                              {'form': form},
                              context_instance=RequestContext(request))

def ws_page(request, ws_pk):
    w = get_object_or_404(Works, pk=ws_pk)
    is_edit = request.user.is_authenticated() and request.user == w.creater # 当前作品是否是当前用户发布的
    return render_to_response('works/ws_page.html',
                              {
                                  'w': w,
                                  'is_edit': is_edit,
                                  },
                              context_instance=RequestContext(request))

@login_required
def ws_edit(request, ws_pk):
    ws = get_object_or_404(Works, pk=ws_pk)
    if request.user != ws.creater:
        return HttpResponseForbindden()
    if request.method == 'POST':
        form = WorksForm(request.POST, instance=ws)
        if form.is_valid():
            model = form.save()
            return HttpResponseRedirect(model.get_absolute_url())
    else:
        form = WorksForm(instance=ws)

    return render_to_response('works/ws_create.html',
                              {'form': form},
                              context_instance=RequestContext(request))





