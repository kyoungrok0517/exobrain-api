from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

class Command(BaseCommand):
    help = "Prepare KCG triples"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        call_command('download_triples')
        call_command('insert_triples')
