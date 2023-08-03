import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS

EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

def print_metadata(filename):
    image = Image.open(filename)
    print(f'Filename: {filename}')
    imgExif = image.getexif()
    if imgExif is None:
        print('No metadata found')
    else:
        for tag_id, value in imgExif.items():
            tag_name = TAGS.get(tag_id, tag_id)
            print(f"{tag_name}: {value}")



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python scorpion.py FILE1 [FILE2 ...]')
        sys.exit(1)

    for arg in sys.argv[1:]:
        if os.path.isfile(arg) and any(arg.endswith(ext) for ext in EXTENSIONS):
            print_metadata(arg)
        else:
            print(f'{arg} is not a valid image file')