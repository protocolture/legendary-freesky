import osimport random

from PIL import Image
from escpos.printer import Usb

# Printer setup
# Replace Vendor id and Product id with the values for your printer
# You might find these using "lsusb" command in Linux
p = Usb(0x04b8, 0x0202, 0)

# Get a random image from the 'ports' directory
try:
    image_name = random.choice([f for f in os.listdir("ports") if f.endswith(".jpg")])
    im = Image.open(os.path.join("ports", image_name))
except IndexError:
    print("No images found in 'ports' directory")
    im = None  # No image to print

# Get a random character file from the 'chars' directory
try:
    char_name = random.choice([f for f in os.listdir("chars") if f.endswith(".txt")])
    with open(os.path.join("chars", char_name), 'r') as file:
        char_details = file.read()
except IndexError:
    print("No text files found in 'chars' directory")
    char_details = "No character details available."

# DPI of the printer and new width in mm
dpi = 203  # common for many receipt printers, but please check for yours
new_width_mm = 40  

if im:
    # Resize image to 40mm width while maintaining aspect ratio
    original_width, original_height = im.size
    new_width_px = int((new_width_mm / 25.4) * dpi) 
    new_height_px = int((new_width_px/original_width) * original_height)
    resized_im = im.resize((new_width_px, new_height_px), Image.ANTIALIAS)

    # Print the image
    p.image(resized_im)
    p.text("\n")

# Print text
p.text(char_details + "\n")

# Cut the paper
p.cut()