from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import ShortnerURL

# Create your views here.
def shortner_url_view(response, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(ShortnerURL, shortcode=shortcode)
    return HttpResponse('Redirect url is {}'.format(obj.url))

class ShortnerCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortnerURL, shortcode=shortcode)
        return HttpResponse('Redirect url is {}'.format(obj.url))
