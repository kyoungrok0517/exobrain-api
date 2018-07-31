from django.core.management.base import BaseCommand, CommandError
import requests
import gzip
from tqdm import tqdm
from pathlib import Path

class Command(BaseCommand):
    help = "Download KCG triples for API"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        self.stdout.write('Downloading triples...')
        url = 'https://storage.googleapis.com/exobrain/data/kcg-triples.json.gz'
        out_dir = Path('./data')
        if not out_dir.is_dir():
            out_dir.mkdir()
        download_path = out_dir / 'kcg-triples.json.gz'
        try:
            r = requests.get(url, stream=True)
        except Exception as e:
            self.stderr.write(e)

        with open(download_path, 'wb') as fout:
            pbar = tqdm(r.iter_content(chunk_size=128))
            for chunk in pbar:
                fout.write(chunk)
