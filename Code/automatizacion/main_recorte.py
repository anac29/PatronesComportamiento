from PIL import Image

import os



def recorte(image):


    # Opens a image in RGB mode
    print(image)
    im = Image.open(image)

    # Setting the points for cropped image
    left = 50
    top = 50
    right = 557
    bottom = 320

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))

    parts=image.split("/")
    im1.save("./cropped/"+parts[8])

    # Shows the image in image viewer

def iterador_archivos():

    # assign directory
    directory = '/home/ana/Documentos/TFG/traffic/output/daily'

    # iterate over files in
    # that directory
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            recorte(f)




if __name__ == '__main__':
    iterador_archivos()
