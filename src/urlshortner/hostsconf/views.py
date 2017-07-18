from django.http import HttpResponseRedirect
from django_hosts.resolvers import reverse
from django.conf import settings


def wildcard_redirect(request, path=None):
    DEFAULT_REDIRECT_URL = getattr(settings, 'DEFAULT_REDIRECT_URL', 'http://www.'+request.META['SERVER_NAME']+':'+request.META['SERVER_PORT'])
    DEFAULT_REDIRECT_URL = 'http://www.'+request.META['SERVER_NAME']+':'+request.META['SERVER_PORT']
    print(DEFAULT_REDIRECT_URL)
    new_url = DEFAULT_REDIRECT_URL
    if path is not None:
        new_url = DEFAULT_REDIRECT_URL+"/"+path
    return HttpResponseRedirect(new_url)
