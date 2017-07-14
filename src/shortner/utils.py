import string
import random


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=6):
    shortcode = code_generator(size=size)
    ShortnerURL = instance.__class__
    qs_exists = ShortnerURL.objects.filter(shortcode=shortcode).exists()
    if qs_exists:
        create_shortcode(size=size)
    return shortcode
