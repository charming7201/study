from PIL import Image

reduce = int(input('please input the reduce times'))

image = Image.open('a.jpg')

'''黑白化图片'''
# image = image.convert('L')

'''resize图片'''
size = image.size
print(size)
weight, height = size
image = image.resize((weight // reduce, height // reduce))

image.show()
image.save('new.jpg')
