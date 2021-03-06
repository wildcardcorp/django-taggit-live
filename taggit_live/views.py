from django.http import HttpResponse
from taggit.models import Tag
from django.utils.datastructures import MultiValueDictKeyError
try:
    from django.utils import simplejson
except ImportError:
    import json as simplejson


def taggit_autocomplete_list(request):
    try:
        q_list = request.GET['term'].split(",")
        q = q_list[len(q_list) - 1]
        results = Tag.objects.filter(
            name__istartswith=q).values_list('name', flat=True)
        tags = ["%s" % x for x in results]
    except MultiValueDictKeyError:
        tags = []
        pass
    return HttpResponse(simplejson.dumps(tags))
