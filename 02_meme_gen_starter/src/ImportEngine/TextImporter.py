from typing import List

from src.QuoteEngine import QuoteModel
from .ImportInterface import ImportInterface


class TextImporter(ImportInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        with open(path, 'r') as f:
            items = []

            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    body = parse[0].strip('"')
                    author = parse[1]
                    new_item = QuoteModel(body, author)
                    items.append(new_item)

        return items

