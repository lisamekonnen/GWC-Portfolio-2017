from PIL import Image

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Import image.
my_image = Image.open("Steve_McCurry.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

#list that will hold the pixel data for the new image.
recolored = []

# Create a new image using the recolored list. Display and save the image.
for pixels in image_list:
    add = pixels[0] + pixels[1] + pixels[2]
    if add <=182:
        pixels=darkBlue
        recolored.append(darkBlue)
    elif 182<add and add<=364:
        pixels=red
        recolored.append(red)
    elif 364<add and add<=546:
        pixels=lightBlue
        recolored.append(lightBlue)
    elif (add> 546):
        pixels=yellow
        recolored.append(yellow)


#New Image
    #New Image
new_image = Image.new("RGB",  my_image.size)
    #Creates a new image that will be the same size as the original image.
new_image = Image.new("RGB", my_image.size)

    #Adds the data from the recolored list to the image.
new_image.putdata(recolored)

    #Show the new image on the screen
new_image.show()

    #Save the new image as "recolored.jpg"
new_image.save("recolored.jpg", "jpeg")
