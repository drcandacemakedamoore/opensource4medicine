#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from collections import namedtuple

import pandas as pd
import numpy as np
import os

from PIL import Image


Rectangle = namedtuple('Recltangle', 'x,y,width,height')

parser = ArgumentParser(
    '''
    Compare two rectangular areas of an image
    '''
)
parser.add_argument(
    '--rectangle1',
    nargs=4,
    type=int,
    required=True,
    help='''
    X, Y, Width and Height of the first rectangle to compare
    ''',
)
parser.add_argument(
    '--rectangle2',
    nargs=4,
    type=int,
    required=True,
    help='''
    X, Y, Width and Height of the second rectangle to compare
    ''',
)
parser.add_argument(
    'image',
    help='''
    The image whose areas to compare
    ''',
)


def split_and_avg_channels(sample):
    return (
        sample[:, :, 0].mean(),
        sample[:, :, 1].mean(),
        sample[:, :, 2].mean(),
    )


def main():
    args = parser.parse_args()
    image = Image.open(args.image)
    nparray = np.array(image)
    sample_rect1 = Rectangle(*args.rectangle1)
    sample_rect2 = Rectangle(*args.rectangle2)
    sample1 = nparray[
        sample_rect1.y : sample_rect1.y + sample_rect1.height,
        sample_rect1.x : sample_rect1.x + sample_rect1.width
    ]
    sample2 = nparray[
        sample_rect2.y : sample_rect2.y + sample_rect2.height,
        sample_rect2.x : sample_rect2.x + sample_rect2.width
    ]
    r1, g1, b1 = split_and_avg_channels(sample1)
    r2, g2, b2 = split_and_avg_channels(sample2)
    print('R1 = {}, G1 = {}, B1 = {}'.format(r1, g1, b1))
    print('R2 = {}, G2 = {}, B2 = {}'.format(r2, g2, b2))

main()
# with love from makeda and oleg