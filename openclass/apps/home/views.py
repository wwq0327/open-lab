from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from events.models import Event
from projects.models import PrjFollower
#@login_required
def index(request):
    es = Event.objects.all()
    #u = User.objects.get(username=request.user.username)
    if request.user.is_authenticated():
        count = PrjFollower.objects.filter(follower=request.user).count()
    else:
        count = None

    return render_to_response('home/index.html',
                              {'events': es,
                               'get_follow': count},
                              context_instance=RequestContext(request))
