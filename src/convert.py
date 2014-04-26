#-*- coding: utf-8 -*-
import sys

from PIL import Image


MAX_LEN = 100.0
FIX_RATE = 2.3
REPLACEMENT = 'MNHQ$OC?7>!:-;. '


def convert(filename, max_len=MAX_LEN, fix_rate=FIX_RATE):
    image = Image.open(filename)
    image = image.convert('L')

    width, height = image.size
    rate = max_len / max(width, height)
    width = int(rate * width)
    height = int(rate * height / fix_rate)

    image = image.resize((width, height))

    data = image.load()

    output = ''

    for h in xrange(height):
        for w in xrange(width):
            output += REPLACEMENT[int(data[w, h] / 256.0 * 16)]
        output += '\n'

    print output


if __name__ == '__main__':
    ml = MAX_LEN
    fr = FIX_RATE
    if len(sys.argv) >= 3:
        ml = sys.argv[2]
    if len(sys.argv) >= 4:
        fr = sys.argv[3]
    convert(sys.argv[1], ml, fr)
