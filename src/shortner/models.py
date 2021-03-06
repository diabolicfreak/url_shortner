from django.db import models
from .utils import create_shortcode

from django_hosts.resolvers import reverse
from django.conf import settings
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)

class ShortnerManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(ShortnerManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        new_codes=0
        qs = ShortnerURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return "New codes generated: {i}".format(i=new_codes)

class ShortnerURL(models.Model):
    url         = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode   = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    active      = models.BooleanField(default=True)

    objects     = ShortnerManager()

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def save(self, *args, **kwargs):
        if not "http" in self.url:
            self.url = "http://"+self.url
        if self.shortcode is None or self.shortcode == '':
            self.shortcode=create_shortcode(self)
        super(ShortnerURL, self).save(*args, **kwargs)

    def get_short_url(self):
        homepage_url = reverse('shortcode', host='www', kwargs={'shortcode': self.shortcode})
        return "{shortcode}".format(shortcode=homepage_url)
