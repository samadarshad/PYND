from ImportEngine import Importer
from ImageEngine import MemeEngine

if __name__ == "__main__":
    # parsed = Importer.parse("_data/SimpleLines/SimpleLines.txt")
    # print(parsed)
    #
    # parsed = Importer.parse("_data/SimpleLines/SimpleLines.csv")
    # print(parsed)
    #
    # parsed = Importer.parse("_data/SimpleLines/SimpleLines.pdf")
    # print(parsed)
    #
    # parsed = Importer.parse("_data/SimpleLines/SimpleLines.docx")
    # print(parsed)

    meme = MemeEngine('./tmp')
    print(meme.make_meme('/Users/samadarshad/dev/PYND/02_meme_gen_starter/src/_data/photos/dog/xander_2.jpg', 'hey', 'sam'))
