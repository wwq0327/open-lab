from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from events.models import Event

#@login_required
def index(request):
    es = Event.objects.all()

    return render_to_response('home/index.html',
                              {'events': es},
                              context_instance=RequestContext(request))
