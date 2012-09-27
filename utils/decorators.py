from functools import wraps
import json
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

class JsonResponse(HttpResponse):
    """
    HttpResponse descendant, which return response with ``application/json`` mimetype.
    """
    def __init__(self, data):
        super(JsonResponse, self).__init__(content=json.dumps(data), mimetype='application/json; charset=utf-8')


def ajax_request(func):
    """
    If view returned serializable dict, returns JsonResponse with this dict as content.

    example:

        @ajax_request
        def my_view(request):
            news = News.objects.all()
            news_titles = [entry.title for entry in news]
            return {'news_titles': news_titles}
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        if isinstance(response, HttpResponse):
            return response
        else:
            return JsonResponse(response)
    return wrapper