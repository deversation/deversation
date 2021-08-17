# pillow import
# pip install pillow
# poetry add pillow
import PIL.Image
# Kite tutorial ASCII IMAGES
# https://www.youtube.com/watch?v=v_raWlX7tZY&t=150s

ASCII = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.' ]

def resize_img(img, new_width=50):
    width, height = img.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resize_img = img.resize((new_width, new_height))
    return(resize_img)

def greyscale(img):
    greyscale_img = img.convert('L')
    return(greyscale_img)

def pixels_to_ascii(img):
    pixels = img.getdata() 
    characters = ''.join([ASCII[pixel//25] for pixel in pixels])
    return (characters)

def main(new_width=100):
    # path = input("Enter a valid pathname to an image:\n")
    # path = 'astro.png'
    path = 'apple.jpg'
    try:
        img = PIL.Image.open(path)
    except:
        print(path, "not valid")
        return

    new_img = pixels_to_ascii(greyscale(resize_img(img)))
    pixel_count = len(new_img)
    ascii_img = "\n".join([new_img[i: (i+new_width)] for i in range(0, pixel_count, new_width)])

    print(ascii_img)

    with open("ascii_image.txt", "W") as file:
        file.write(ascii_img)


# def bio():
#     bio_path = 'bio.txt'
#     with open(bio_path) as file:
#         file.read()
#         print(file)


main()
# bio()

# --------
# Pixled images to terminal
# poetry add climage
# https://github.com/pnappa/CLImage
# import climage
  
# # converts the image to print in terminal
# # inform of ANSI Escape codes
# # output = climage.convert('assets/harold.jpg')
# # more detail
# output = climage.convert('assets/harold.jpg', is_unicode=True)
# print(output)
