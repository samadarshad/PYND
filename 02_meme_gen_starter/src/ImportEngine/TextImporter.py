from typing import List

from QuoteEngine import QuoteModel
from .ImportInterface import ImportInterface
from .helper import parse_text_line


class TextImporter(ImportInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        with open(path, 'r') as f:
            items = []

            for line in f.readlines():
                try:
                    items.append(QuoteModel(*parse_text_line(line)))
                except IndexError as e:
                    pass

        return items
