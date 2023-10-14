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

# Format and print text
p.text("\n")  # Add an empty line after the image
p.set(align="center")
p._raw(b'\x1b!\x30')  # Set to bold, double-height, and double-width
p.text(char_details.split('\n')[0] + "\n")  # Print name

p._raw(b'\x1b!\x00')  # Reset to normal text size and weight
p.set(align="left")
wrapped_text = textwrap.wrap(char_details, width=40)  # Adjust width as per requirements
for line in wrapped_text[1:]:
    p.text(line + "\n")

p.cut()
Explanation
p._raw(b'\x1b!\x30'): Sends raw commands to adjust the text size and style. \x30 will typically set the text to be double-width, double-height, and bold in ESC/POS.
p._raw(b'\x1b!\x00'): Resets the text to its normal size and style.
Note
The correct byte sequences can sometimes depend on the printer model. If the above does not work as expected, you might need to consult your printer's ESC/POS command guide.

Test and Modify
It’s crucial to test and adjust as per your requirements and hardware. If any character doesn’t render as expected, it’s worthwhile looking into the specific ESC/POS commands supported by your printer model. And always make sure to follow any guidelines provided in the official documentation or community resources for python-escpos.





