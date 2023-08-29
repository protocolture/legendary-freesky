#!/usr/bin/env python3
import subprocess

HOST="192.168.20.59"
# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND="sudo python3 /freesky/legendary-freesky/dskyrelay/relaytest3.py"

def main():
 
    ssh = subprocess.Popen(["ssh matt@192.168.109.59 -p matt", "%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()

    print("This is the stub script for code dc.") 
    
    if result == []:
        error = ssh.stderr.readlines()
        print >>sys.stderr, "ERROR: %s" % error
    else:
        print (result)
    
if __name__ == '__main__':
    main()
