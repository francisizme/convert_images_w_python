# !/usr/bin/env python3
# Use the Python Imaging Library to do the following to a batch of images:
#
# Open an image
#
# Rotate an image
#
# Resize an image
#
# Save an image in a specific format in a separate directory
import os
from PIL import Image

os.chdir('images')  # change this to your demand input sources
for file in os.listdir():
    file_name, ext = os.path.splitext(file)
    outfile = '/opt/icons/' + file_name + '.jpeg'
    try:
        if os.path.isfile(file):
            with Image.open(file) as im:
                im.convert('RGB').resize((128, 128)).rotate(-90).save(outfile)
    except OSError:
        print('cannot convert', file)
