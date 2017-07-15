from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def shortner_url_view(response, shortcode=None, *args, **kwargs):
    print(shortcode)
    return HttpResponse('Hello method')

class ShortnerCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        print(shortcode)
        return HttpResponse('Hello cbv')
