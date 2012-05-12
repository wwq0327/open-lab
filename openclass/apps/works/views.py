#! -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from works.models import Works
from works.forms import WorksForm

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
            model = form.save(request.user)
            return HttpResponseRedirect(model.get_absolute_url())
    else:
        form = WorksForm()

    return render_to_response('works/ws_create.html',
                              {'form': form},
                              context_instance=RequestContext(request))

def ws_page(request, ws_pk):
    w = get_object_or_404(Works, pk=ws_pk)

    return render_to_response('works/ws_page.html',
                              {
                                  'w': w,
                                  },
                              context_instance=RequestContext(request))




