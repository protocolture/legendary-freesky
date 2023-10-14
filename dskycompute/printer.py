import os
from PIL import Image
from escpos.printer import Usb

# Printer setup
# Replace Vendor id and Product id with the values for your printer
# You might find these using "lsusb" command in Linux
p = Usb(0x04b8, 0x0202, 0)

# Load and print the image
image_path = "ports/port8.jpg"
original_image = Image.open(image_path)
target_width_mm = 40  # ~90% of 80mm
target_width_px = int((target_width_mm / 25.4) * 203)  # 203dpi is a common print density for thermal printers

# Resize image to fit width of paper
w_percent = (target_width_px / float(original_image.size[0]))
target_height_px = int((float(original_image.size[1]) * float(w_percent)))
resized_image = original_image.resize((target_width_px, target_height_px), Image.ANTIALIAS)

# Print image
p.image(resized_image)

# Load character details
char_file_path = "chars/char1.txt"
with open(char_file_path, "r") as file:
    char_details = file.read()

# Format and print the text
p.set(align="center")
p.set_text_size(2, 2)  # double width and height
p.text(char_details.split('\n')[0] + "\n")  # Print name
p.set_text_size(1, 1)  # Reset to normal size for rest

p.set(align="left")
for line in wrapped_text[1:]:
    p.text(line + "\n") # Reset to normal size for rest
wrapped_text = textwrap.wrap(char_details, width=32)  # Wrap text at approx 32 chars per line

# Skip printing the name again
for line in wrapped_text[1:]:
    p.text(line + "\n")

# Ensure to cut the paper after printing
p.cut()

# Close the connection to the printer
p.close()