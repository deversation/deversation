import climage
# import PIL.Image

'''
Converts image files to characters defined in ASCII
'''
# ASCII = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.' ]

# def resize_img(img, new_width=50):
#     width, height = img.size
#     ratio = height / width
#     new_height = int(new_width * ratio)
#     resize_img = img.resize((new_width, new_height))
#     return(resize_img)

# def greyscale(img):
#     greyscale_img = img.convert('L')
#     return(greyscale_img)

# def pixels_to_ascii(img):
#     pixels = img.getdata() 
#     characters = ''.join([ASCII[pixel//25] for pixel in pixels])
#     return (characters)

# def main(new_width=100):
#     # path = input("Enter a valid pathname to an image:\n")
#     # path = 'astro.png'
#     path = '../assets/apple.jpg'
#     try:
#         img = PIL.Image.open(path)
#     except:
#         print(path, "not valid")
#         return

#     new_img = pixels_to_ascii(greyscale(resize_img(img)))
#     pixel_count = len(new_img)
#     ascii_img = "\n".join([new_img[i: (i+new_width)] for i in range(0, pixel_count, new_width)])

#     print(ascii_img)

# main()

def bio(user):
    '''
    Reads from bio.txt file and sends information to client. Prints images to server.
    '''
    output1 = climage.convert('../assets/anthony.jpg', is_unicode=True, width=20)
    output2 = climage.convert('../assets/tony.jpg', is_unicode=True, width=20)
    output3 = climage.convert('../assets/wonde.jpg', is_unicode=True, width=20)
    output4 = climage.convert('../assets/marie.jpg', is_unicode=True, width=20)
    print(output1)
    print(output2)
    print(output3)
    print(output4)
    with open('../assets/bio.txt', 'rb') as f:
        bio = f.read()
        user.socket.sendall(bio)


# image over sockets
# def bio_img(user):
#     with open('../assets/harold.jpg', 'wb') as f:
#         bio_img = f.read()
#         user.socket.sendall(bio_img)
    # with open('../assets/harold.jpg', 'wb') as n:
    #     bio_imgs = n.write()
    #     user.socket.sendall(bio_imgs)


    

    
