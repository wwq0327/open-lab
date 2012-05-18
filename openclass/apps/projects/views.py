#! -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from projects.models import Projects, PriFollower, top_comments
from projects.forms import ProjectsForm

def index(request):
    prjs = Projects.objects.all()
    new_prj = Projects.objects.all()[:10]

    return render_to_response('projects/index.html',
                              {
                                  'prjs': prjs,
                                  'top_comments': top_comments(),
                                  'new_prj': new_prj,
                                  },
                              context_instance=RequestContext(request))

@login_required
def prj_create(request):
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.creater = request.user
            model.save()
            return HttpResponseRedirect(model.get_absolute_url())
    else:
        form = ProjectsForm()

    return render_to_response('projects/prj_create.html',
                              {'form': form},
                              context_instance=RequestContext(request))

def prj_page(request, prj_pk):
    p = get_object_or_404(Projects, pk=prj_pk)
    c_user = get_object_or_404(User, username=p.creater.username)
    profile = c_user.get_profile()
    return render_to_response('projects/prj_page.html',
                              {'p': p,
                               'profile': profile,
                               },
                              context_instance=RequestContext(request))

def prj_follow(request, prj_pk):
    p = get_object_or_404(Projects, pk=prj_pk)

    obj, create = PrjFollower.objects.get_or_creater(
        follower=request.user,
        project=p)
    if create:
        pass
    obj.save()

    return HttpResponseRedirect(p.get_absolute_url())


