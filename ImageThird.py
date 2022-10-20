from PIL import Image

'''
Convert Image...
'''
def main():
    file_name='Google.png'
    image = Image.open(file_name)
    image.convert(mode='L',dither=16).show();
    del image
    
    
if __name__ == '__main__':
    main()