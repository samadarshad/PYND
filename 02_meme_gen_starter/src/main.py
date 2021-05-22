from ImportEngine import Importer

if __name__ == "__main__":
    parsed = Importer.parse("_data/SimpleLines/SimpleLines.txt")
    print(parsed)