from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.views import View
from .models import ShortnerURL
from .forms import SubmitUrlForm
from analytics.models import ClickEvent

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
        template = 'shortner/home.html'
        context = {
            'title': 'Submit url title',
            'form': form
        }
        if form.is_valid():
            print(form.cleaned_data)
            url = form.cleaned_data.get('url')
            obj, created = ShortnerURL.objects.get_or_create(url=url)
            context = {
                'title': 'Shortcode',
                'obj': obj
            }
            if created:
                template = 'shortner/success.html'
            if not created:
                template = 'shortner/already-exists.html'

        return render(request, template, context)


class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ShortnerURL, shortcode=shortcode)
        ClickEvent.objects.create_event(obj)
        print(obj.url)
        if not "http://" in obj.url:
            obj.url = "http://" + obj.url
        # return HttpResponse('Redirect url is {}'.format(obj.url))
        return HttpResponseRedirect(obj.url)
