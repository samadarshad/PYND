
from typing import List
import docx

from .ImportInterface import ImportInterface
from QuoteEngine import QuoteModel


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
                line = para.text
                parse = line.split(' - ')
                body = parse[0].strip('"')
                author = parse[1]
                new_item = QuoteModel(body, author)
                items.append(new_item)

        return items
