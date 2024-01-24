'''jpeg to png converter'''
import os
import sys
import PIL.Image

jpeg_folder = sys.argv[1]
png_folder = sys.argv[2]

print(os.path.exists(jpeg_folder))
print(os.path.exists(png_folder))
if not os.path.exists(png_folder):
    os.makedirs(png_folder)

for filename in os.listdir(jpeg_folder):
    try:
        img = PIL.Image.open(f'{jpeg_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{png_folder}{clean_name}.png', 'png')
        print('all done')
    except PIL.UnidentifiedImageError:
        print(f"Skipped non-image file: {filename}")
