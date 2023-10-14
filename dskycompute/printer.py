import os
from PIL import Image
from escpos.printer import Usb

# Setup
p = Usb(0x04b8, 0x0e15, 0)

try:
    # Set text size
    p.set(font='a', height=1, width=1)

    # Print text
    p.text("Hello, here is your receipt with an image!\n")

    # Load and resize the image
    base_path = os.path.dirname(os.path.abspath(__file__))  # Get script directory
    image_path = os.path.join(base_path, "ports", "port8.jpg")
    original_image = Image.open(image_path)
    
    # Assuming 80mm wide paper, with 203DPI typical on Epson printers
    # Resizing to 90% of paper width
    target_width_mm = 72
    dpi = 203
    target_width_px = int((target_width_mm / 25.4) * dpi)
    
    # Maintain aspect ratio during resize
    w_percent = (target_width_px / float(original_image.size[0]))
    target_height_px = int((float(original_image.size[1]) * float(w_percent)))
    
    resized_image = original_image.resize((target_width_px, target_height_px), Image.ANTIALIAS)
    
    # Print image
    p.image(resized_image)
    
    # Additional text
    p.text("Here's more text after the image.\n")
    
    # Cut the paper
    p.cut()

finally:
    # Ensure the device is properly reset for next print
    p.device.close()