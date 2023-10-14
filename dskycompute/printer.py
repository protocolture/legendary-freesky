from escpos.printer import Usb

# Printer setup
# Replace Vendor id and Product id with the values for your printer
# You might find these using "lsusb" command in Linux
p = Usb(0x04b8, 0x0202, 0)

try:
    # Set the text size: 1x size for both vertical and horizontal
    # This can be adjusted as per need
    p.set(font='a', height=1, width=1)

    # Text output
    p.text("Hello, this is your Epson printer speaking!\n")
    p.text("Here's a line of small text.\n")
    
    # Set the text size: 2x size for both vertical and horizontal
    p.set(height=2, width=2)
    p.text("And here is bigger text!\n")

    # Cut the paper
    p.cut()

finally:
    # Ensure the device is properly reset for next print
    p.device.close()