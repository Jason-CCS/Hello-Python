"""
使用Pillow操作影像
"""
from PIL import Image

# create img

im = Image.new('RGBA', (256, 256), 'navy')
im.save('navy.png')

# read img
navy = Image.open('navy.png')
print(navy.size)
print(navy.filename)
print(navy.format)
print(navy.format_description)
# print(ImageColor.getcolor('red', 'RGBA'))

# update img
navy_cropped = navy.crop((0, 0, 50, 50))
print(navy_cropped.size)
navy_cropped.save('cropped-navy.png')

# paste
black = Image.new('RGBA', (256, 256), 'black')
black.paste(navy_cropped, (0, 0))
black.save('black_paste.png')

# resize
black_paste = Image.open('black_paste.png')
black_paste.resize((100, 100)).save('resize01.png')
black_paste.resize((100, 500)).save('resize02.png')

# rotate
black_paste.rotate(90).save('rotate90.png')
black_paste.rotate(180).save('rotate180.png')




