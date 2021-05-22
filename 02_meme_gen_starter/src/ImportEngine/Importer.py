from typing import List

from .ImportInterface import ImportInterface
from src.QuoteEngine import QuoteModel
from .DocxImporter import DocxImporter
from .CSVImporter import CSVImporter
from .PDFImporter import PDFImporter
from .TextImporter import TextImporter


class Importer(ImportInterface):
    importers = [DocxImporter, CSVImporter, PDFImporter, TextImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        print(path)
        for importer in cls.importers:
            if importer.can_ingest(path):
                return importer.parse(path)
