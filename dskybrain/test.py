import subprocess
import time

def run_kasa_command(host, action, index, device_type="strip"):
    cmd = ["kasa", "--type", device_type, "--host", host, action, "--index", str(index)]
    subprocess.run(cmd)

def main():
    # Turn on index 1 of 192.168.20.148
    run_kasa_command("192.168.20.148", "on", 1)
    time.sleep(2)
    
    # Run the remaining commands without delay
    commands = [
        ("192.168.20.148", "on", 0),
        ("192.168.20.63", "on", 0),
        ("192.168.20.64", "on", 0),
        ("192.168.20.64", "on", 1),
        ("192.168.20.64", "on", 2),
    ]
    for host, action, index in commands:
        run_kasa_command(host, action, index)
    
    time.sleep(2)
    
    # Turn off index 1 of 192.168.20.148
    run_kasa_command("192.168.20.148", "off", 1)

if __name__ == "__main__":
    main()