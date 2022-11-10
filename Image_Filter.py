from PIL import Image,ImageFilter

'''
Reading an image given
'''
def main():
    file_name='Google.png'
    image=Image.open(file_name)
    image.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
    # image.save()
    del image

if __name__ == '__main__':
    main()