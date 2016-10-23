from django.core.management.base import BaseCommand, CommandError
from shoortner.models import *

class Command(BaseCommand):
    help = 'Refrechs all short code'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)




    def handle(self, *args, **options):
        return KssirURL.objects.refresh_shortcodes(items=options['items'])