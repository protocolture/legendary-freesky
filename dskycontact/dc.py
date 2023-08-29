#!/usr/bin/env python3
import subprocess

def main():
    print("This is the stub script for code dc.") 
    subprocess.Popen(f"ssh -p matt matt@192.168.20.59 python3 /RPi_Relay_Board_B/RaspberryPi/python/relaytest3.py", shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
if __name__ == '__main__':
    main()
