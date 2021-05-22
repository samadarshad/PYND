from typing import List
import subprocess
import os
import random

from .ImportInterface import ImportInterface
from src.QuoteEngine import QuoteModel

pdftotext = '/Users/samadarshad/dev/PYND/02_meme_gen_starter/third_party/xpdf-tools-mac-4.03/bin64/pdftotext'


class PDFImporter(ImportInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0, 10000)}.txt'
        call = subprocess.call([pdftotext, '-layout', path, tmp])

        with open(tmp, 'r') as f:
            items = []

            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    body = parse[0].strip('"')
                    author = parse[1]
                    new_item = QuoteModel(body, author)
                    items.append(new_item)

        os.remove(tmp)
        return items
