# install and import pillow
# open up the image you want to resize using python
# print the current size of the image
# specify the size we wanna change it too
# save the new sized image


from PIL import Image


def resize(size1,size2):

    image=Image.open('githubimage.jpeg')
    print(f"Current size:{image.size}")

    resized_image=image.resize((size1,size2))
    resized_image.save("githubresized.jpeg")

size1=int(input("Enter width: "))
size2=int(input("Enter Length: "))
resize(size1,size2)
