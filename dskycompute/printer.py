import os
from PIL import Image
from escpos.printer import Usb

# Printer setup
# Replace Vendor id and Product id with the values for your printer
# You might find these using "lsusb" command in Linux
p = Usb(0x04b8, 0x0202, 0)

# Open image, resize, and print it
im = Image.open(os.path.join("ports", "port8.jpg"))
width, height = im.size
new_width = int(width * 0.9)
new_height = int(height * (new_width / width))
resized_im = im.resize((new_width, new_height), Image.ANTIALIAS)
p.image(resized_im)

# Load and format character details
with open(os.path.join("chars", "char1.txt"), 'r') as file:
    char_details = file.read()

# Print text
p.text("\n")  # Add an empty line after the image
p.text(char_details + "\n")

# Cut the paper
p.cut()




