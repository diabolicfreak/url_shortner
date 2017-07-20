from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.views import View
from .models import ShortnerURL

from .forms import SubmitUrlForm

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
            'title': 'Submit url title',
            'form': form
        }
        return render(request, 'shortner/home.html', context)

    def post(self, request, *args, **kwargs):
        # print(request.POST.get('url'))
        form = SubmitUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        context = {
            'title': 'Submit url title',
            'form': form
        }
        return render(request, 'shortner/home.html', context)


class ShortnerCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortnerURL, shortcode=shortcode)
        return HttpResponse('Redirect url is {}'.format(obj.url))
