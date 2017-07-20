from django.db import models
from shortner.models import ShortnerURL

class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(instance, ShortnerURL):
            obj, created = self.get_or_create(shortner_url=instance)
            obj.count += 1
            obj.save()
            print(obj.count)
            return obj.count

class ClickEvent(models.Model):
    shortner_url    = models.OneToOneField(ShortnerURL)
    count           = models.IntegerField(default=0)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{i}".format(i=self.shortner_url)

    objects = ClickEventManager()
