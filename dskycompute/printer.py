import os
from PIL import Image
from escpos.printer import Usb

# Printer setup
# Replace Vendor id and Product id with the values for your printer
# You might find these using "lsusb" command in Linux
p = Usb(0x04b8, 0x0202, 0)

# Open image, resize, and print it
im = Image.open(os.path.join("ports", "port8.jpg"))
original_width, original_height = im.size

# DPI of the printer
dpi = 203  # common for many receipt printers, but please check for yours

# Set new width and calculate the new height maintaining the aspect ratio
new_width_mm = 40  # Width in mm
new_width_px = int((new_width_mm / 25.4) * dpi)  # Convert mm to inches, then multiply by DPI for px
new_height_px = int((new_width_px/original_width) * original_height)

# Resize and print the image
resized_im = im.resize((new_width_px, new_height_px), Image.ANTIALIAS)
p.image(resized_im)

# Load and format character details
with open(os.path.join("chars", "char1.txt"), 'r') as file:
    char_details = file.read()

# Print text
p.text("\n")  # Add an empty line after the image
p.text(char_details + "\n")

# Cut the paper
p.cut()