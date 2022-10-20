from turtle import width
from PIL import Image


'''
main function here! create a png image for the given size and color 
'''
def main():
    size = width,height = 320,240;
    image = Image.new("RGB", size , 'White')
    image.show()
    
    del image
    
#call the functions!
if __name__ == '__main__':
    main()