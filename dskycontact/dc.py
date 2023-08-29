#!/usr/bin/env python3
import paramiko


HOST="192.168.20.59"
# Ports are handled in ~/.ssh/config since we use OpenSSH
COMMAND="sudo python3 /freesky/legendary-freesky/dskyrelay/relaytest3.py"

def main():
 
    ssh = paramiko.SSHClient()

    print("This is the stub script for code dc.") 
    
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
    ssh.connect('192.168.20.59', port=22, username='matt',
            password='matt', timeout=3)
    stdin, stdout, stderr = ssh.exec_command('sudo python3 /freesky/legendary-freesky/dskyrelay/relaytest3.py')
    
if __name__ == '__main__':
    main()
