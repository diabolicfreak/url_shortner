from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.views import View
from .models import ShortnerURL

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shortner/home.html', {})

class ShortnerCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortnerURL, shortcode=shortcode)
        return HttpResponse('Redirect url is {}'.format(obj.url))
