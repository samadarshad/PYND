from typing import List
import subprocess
import os
import random

from .ImportInterface import ImportInterface
from src.QuoteEngine import QuoteModel


class PDFImporter(ImportInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0, 10000)}.txt'
        call = subprocess.call(['./third_party/xpdf-tools-mac-4.03/bin64/pdftotext', path, tmp])

        file_ref = open(tmp, 'r')
        items = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split(',')
                new_item = QuoteModel(parse[0], parse[1])
                items.append(new_item)

        file_ref.close()
        os.remove(tmp)
        return items