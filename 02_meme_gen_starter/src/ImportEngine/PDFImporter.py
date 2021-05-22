import os
import random
import subprocess
from typing import List

from QuoteEngine import QuoteModel
from .ImportInterface import ImportInterface
from .TextImporter import TextImporter

pdftotext = '/Users/samadarshad/dev/PYND/02_meme_gen_starter/third_party/xpdf-tools-mac-4.03/bin64/pdftotext'


class PDFImporter(ImportInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0, 10000)}.txt'
        call = subprocess.call([pdftotext, '-layout', path, tmp])
        assert call == 0, 'Error in pdftotext call'

        items = TextImporter.parse(tmp)

        os.remove(tmp)
        return items
