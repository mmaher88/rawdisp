import sys
from PIL import Image
def main():
    try:
        rawFile = open(sys.argv[1], "rb")
        rawBytes = rawFile.read()

        if(sys.argv[2] == "nv16"):
            nv16ToRgb(rawBytes)
        else:
            if(sys.argv[2] == "rgbx"):
                rgbxToRgb(rawBytes)
            else:
                print("invalid format")

    except OSError as e:
        print(e.strerror, ":", e.filename)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        rawFile.close()


    
def rgbxToRgb(raw):
    print("not implemented")

def nv16ToRgb(raw):
    print("converting from nv16 to rgb")
    # PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]
    img = Image.new( 'RGB', (1624,1280), "black") # create a new black image
    pixels = img.load() # create the pixel map

    for i in range(img.size[0]):    # for every col:
        for j in range(img.size[1]):    # For every row
            pixels[i,j] = (raw[i + (j * img.size[1])], raw[i + (j * img.size[1])], raw[i + (j * img.size[1])]) # set the colour accordingly

    img.show()

if __name__ == "__main__":
    main()