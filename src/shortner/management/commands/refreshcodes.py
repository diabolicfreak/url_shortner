from django.core.management.base import BaseCommand, CommandError
from shortner.models import ShortnerURL

class Command(BaseCommand):
    help = 'Refresh all shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return ShortnerURL.objects.refresh_shortcodes(options['items'])
