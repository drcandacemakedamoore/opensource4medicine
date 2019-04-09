import os

from argparse import ArgumentParser
from PIL import Image


parser = ArgumentParser(description='Batch image transformer')
parser.add_argument(
    'src',
    default='.',
    help='''
    The source directory containing images.
    ''',
)
parser.add_argument(
    'dst',
    default='transformed',
    help='''
    Destingation directory where the processed images will be saved.
    '''
)

args = parser.parse_args()

try:
    os.makedirs(args.dst)
except OSError as e:
    print(e)

pictures = os.listdir(args.src)
file_currently_reading = 0
file_number_count = len(pictures)
 
while file_currently_reading < file_number_count:
    filename = pictures[file_currently_reading]
    im = Image.open(os.path.join(args.src, filename))
    im = im.transform(
        im.size,
        Image.AFFINE,
        [1, -0.0018, -20, 0.039, 1.0337, -20],
        resample=Image.BICUBIC,
    )
    im.save(os.path.join(args.dst, filename), 'PNG')
    file_currently_reading = file_currently_reading + 1
