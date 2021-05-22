from pathlib import Path

from .generate_postcard import generate_postcard

class MemeEngine:
    def __init__(self, output_dir: str) -> None:
        self.output_dir = Path(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        out_path = self.output_dir / img_path.split('/')[-1]
        message = f'"{text}" - {author}'
        return generate_postcard(img_path, out_path, message, None, width)

