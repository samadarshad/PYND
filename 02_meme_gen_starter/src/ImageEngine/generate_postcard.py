from PIL import Image, ImageDraw, ImageFont


def generate_postcard(in_path, out_path, message=None, crop=None, width=None):
    """Create a Postcard With a Text Greeting

    Arguments:
        in_path {str} -- the file location for the input image.
        out_path {str} -- the desired location for the output image.
        crop {tuple} -- The crop rectangle, as a (left, upper, right, lower)-tuple. Default=None.
        width {int} -- The pixel width value. Default=None.
    Returns:
        str -- the file path to the output image.
    """
    img = Image.open(in_path)

    if crop is not None:
        assert max(crop) < min(
            img.size), 'Warning - may be cropping outside image size, this will return a black image!'
        img = img.crop(crop)

    if width is not None:
        ratio = width / float(img.size[0])
        height = int(ratio * float(img.size[1]))
        img = img.resize((width, height), Image.NEAREST)

    if message is not None:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(
            '/Users/samadarshad/dev/PYND/02_meme_gen_starter/src/ImageEngine/fonts/LilitaOne-Regular.ttf', size=20)
        draw.text((10, 30), message, font=font, fill='white')

    img.save(out_path)
    return out_path


if __name__ == '__main__':
    print(generate_postcard('/Users/samadarshad/dev/PYND/02_meme_gen_starter/src/_data/photos/dog/xander_2.jpg',
                            'out.jpg',
                            'abc',
                            None,
                            # (450, 900, 900, 1300),
                            500))
