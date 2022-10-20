from PIL import Image

'''
Reading an image given
'''
def main():
    file_name='Google.png'
    image=Image.open(file_name)
    image.show()
    
    del image

if __name__ == '__main__':
    main()