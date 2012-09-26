from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def render_with(template):
    def render_with_decorator(view_func):
        def wrapper(*args, **kwargs):
            request = args[0]
            context = view_func(*args, **kwargs)
            if (isinstance(context, HttpResponse)):
                return context
            return render_to_response(
                template,
                context,
                context_instance=RequestContext(request),
            )
        return wrapper
    return render_with_decorator