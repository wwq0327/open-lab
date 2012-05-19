import markdown
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.shortcuts import render_to_response

def about(request):
    tmp = get_template('static/about.txt')
    about_context = tmp.render(Context({}))
    about = markdown.markdown(about_context)

    return render_to_response('static/about.html',
                              {'about': about},
                              context_instance=RequestContext(request))
def contact(request):
    tmp = get_template('static/contact.txt')
    contact_context = tmp.render(Context({}))
    contact = markdown.markdown(contact_context)

    return render_to_response('static/contact.html',
                              {'contact': contact},
                              context_instance=RequestContext(request))
