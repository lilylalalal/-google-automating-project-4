import os,sys
from PIL import Image


def modifypic(pic,directory):
    image=Image.open(directory+pic)
    newpic = pic.replace("tiff", "jpeg")
    im=image.convert('RGB')
    new = im.resize((600,400))
    return new.save(directory+newpic)

def picinfolder(directory):
    file = os.listdir(directory)
    for pic in file:
        if pic.endswith("tiff"):
            newpic = modifypic(pic,directory)
    return newpic

if __name__ == "__main__":
    picinfolder("supplier-data/images/")
