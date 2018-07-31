from django.core.management.base import BaseCommand, CommandError
from kcg.models import Triple
import gzip
import ujson as json
from pathlib import Path

class Command(BaseCommand):
    help = "Insert KCG triples for API"

    def add_arguments(self, parser):
        default_path = Path('./data') / 'kcg-triples.json.gz'
        parser.add_argument('--file_path', type=str, default=default_path)

    def handle(self, *args, **options):
        self.stdout.write('Inserting triples...')
        items = []
        fpath = options['file_path']
        with gzip.open(fpath, 'rt', encoding='utf-8') as fin:
            for i, item in enumerate(fin):
                item = json.loads(item)['fields']
                # explicate `confidence` for ordering
                item['confidence'] = item['rel']['confidence']
                items.append(Triple(**item))
                if i % 1000 == 0:
                    self.stdout.write(f'Processed {i} items')
                    Triple.objects.bulk_create(items)
                    items = []

        # process the remainders
        Triple.objects.bulk_create(items)
