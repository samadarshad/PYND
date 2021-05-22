from typing import List
import pandas

from .ImportInterface import ImportInterface
from src.QuoteEngine import QuoteModel

class CSVImporter(ImportInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        items = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_item = QuoteModel(row['body'], row['author'])
            items.append(new_item)

        return items