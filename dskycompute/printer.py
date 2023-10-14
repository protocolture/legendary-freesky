import os
import random
import redis
from PIL import Image
from escpos.printer import Usb

# Printer setup
# Replace Vendor id and Product id with the values for your printer
# You might find these using "lsusb" command in Linux
p = Usb(0x04b8, 0x0202, 0)

r = redis.Redis(host='localhost', port=6379, db=0)

# Get a random image from the 'ports' directory
try:
    image_name = random.choice([f for f in os.listdir("ports") if f.endswith(".jpg")])
    im = Image.open(os.path.join("ports", image_name))
except IndexError:
    print("No images found in 'ports' directory")
    im = None  # No image to print

# DPI of the printer and new width in mm
dpi = 203
new_width_mm = 40

# Process and print char data if present and True/1 in Redis
for i in range(1, 11):
    char_key = f"char{i}"
    should_print_char = r.get(char_key)
    if should_print_char and int(should_print_char.decode("utf-8")) == 1:
        try:
            with open(os.path.join("chars", f"char{i}.txt"), 'r') as file:
                char_details = file.read()
                
                if im:
                    original_width, original_height = im.size
                    new_width_px = int((new_width_mm / 25.4) * dpi) 
                    new_height_px = int((new_width_px/original_width) * original_height)
                    resized_im = im.resize((new_width_px, new_height_px), Image.ANTIALIAS)

                    p.image(resized_im)
                    p.text("\n")
                
                p.text(char_details + "\n")
                
        except FileNotFoundError:
            print(f"No text file found for {char_key}")

# Process and print note data if present and True/1 in Redis
for i in range(1, 11):
    note_key = f"note{i}"
    should_print_note = r.get(note_key)
    if should_print_note and int(should_print_note.decode("utf-8")) == 1:
        try:
            with open(os.path.join("notes", f"note{i}.txt"), 'r') as file:
                note_details = file.read()
                
                p.text(note_details + "\n")
                
        except FileNotFoundError:
            print(f"No text file found for {note_key}")

# Cut the paper
p.cut()