'''Image processing'''
from PIL import Image, ImageFilter
img = Image.open(
    './jpg_folder/baby_dragon.jpg')
print(img)
print(img.size)
print(img.format)
print(img.mode)
print(dir(img))
# Apply filters like blur, smooth, sharpen:
filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save('blurred_img.png')
filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img.save('smoothened_img.png', 'png')
filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img.save('sharpened_img.png', 'png')
# Convert images:
converted_img = img.convert('L')
# converted_img.save('grey_img.png', 'png')
# converted_img.show()
rotated_img = img.rotate(180)
# rotated_img.show()
resized_img = img.resize((300, 300))
# resized_img.show()
box = [100, 100, 750, 750]
cropped_img = img.crop(box)
# cropped_img.show()
img2 = Image.open('./jpg_folder/astro.jpg')
# img2.show()
# This process of resizing results in compression of the image:
print(img2.size)
new_img2 = img2.resize((400, 400))
# new_img2.save('resized_astro.jpg')
print(new_img2.size)
# new_img2.show()
# Avoid compression using thumbail():
img2.thumbnail((400, 400))
# img2.save('Thumbnail_img.jpg')
print(img2.size)
# img2.show()
