#! -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from projects.models import Projects
from projects.forms import ProjectsForm

def index(request):
    pass

@login_required
def prj_create(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ProjectsForm()

    return render_to_response('projects/prj_create.html',
                              {'form': form},
                              context_instance=RequestContext(request))

def prj_page(request, prj_pk):
    pass
