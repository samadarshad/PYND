
from typing import List
import docx

from .ImportInterface import ImportInterface
from src.QuoteEngine import QuoteModel

class DocxImporter(ImportInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        items = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(',')
                new_item = QuoteModel(parse[0], parse[1])
                items.append(new_item)

        return items