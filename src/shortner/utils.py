import string
import random

from django.conf import settings

SHORTCODE_MIN = getattr(settings, 'SHORTCODE_MIN', 15)

def code_generator(size=SHORTCODE_MIN, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=SHORTCODE_MIN):
    shortcode = code_generator(size=size)
    ShortnerURL = instance.__class__
    qs_exists = ShortnerURL.objects.filter(shortcode=shortcode).exists()
    if qs_exists:
        create_shortcode(size=size)
    return shortcode
