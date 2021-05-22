from ImportEngine import Importer

if __name__ == "__main__":
    parsed = Importer.parse("_data/SimpleLines/SimpleLines.txt")
    print(parsed)

    parsed = Importer.parse("_data/SimpleLines/SimpleLines.csv")
    print(parsed)

    parsed = Importer.parse("_data/SimpleLines/SimpleLines.pdf")
    print(parsed)

    parsed = Importer.parse("_data/SimpleLines/SimpleLines.docx")
    print(parsed)
