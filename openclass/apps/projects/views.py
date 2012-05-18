#! -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from projects.models import Projects, PrjFollower, top_comments
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
    try:
        PrjFollower.objects.get(
            follower__pk=request.user.id,
            project__pk=p.id)
        is_follow = True
    except PrjFollower.DoesNotExist:
        is_follow = False

    return render_to_response('projects/prj_page.html',
                              {'p': p,
                               'profile': profile,
                               'is_follow': is_follow,
                               },
                              context_instance=RequestContext(request))
@login_required
def prj_follow(request, prj_pk):
    p = get_object_or_404(Projects, pk=prj_pk)
    if request.user == p.creater:
        return HttpResponseForbidden()

    obj, created = PrjFollower.objects.get_or_create(
        follower=request.user,
        project=p)
    if not created:
        obj.save()

    return HttpResponseRedirect(p.get_absolute_url())

@login_required
def prj_follow_del(request, prj_pk):
    p = get_object_or_404(Projects, pk=prj_pk)
    f = get_object_or_404(PrjFollower, project__pk=p.id, follower__pk=request.user.id)

    f.delete()
    return HttpResponseRedirect(p.get_absolute_url())


@login_required
def prj_edit(request, prj_pk):
    '''project edit
    @param prj_pk: project id
    '''
    prj = get_object_or_404(Projects, pk=prj_pk)
    if request.user != prj.creater:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = ProjectsForm(request.POST, request.FILES, instance=prj)
        if form.is_valid():
            o = form.save(commit=False)
            o.creater = request.user
            o.save()
            return HttpResponseRedirect(o.get_absolute_url())
    else:
        form = ProjectsForm(instance=prj)

    return render_to_response('projects/prj_create.html',
                              {'form': form},
                              context_instance=RequestContext(request))
