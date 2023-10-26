
#!/usr/bin/env python3


import redis
import subprocess


def main():
    # Connect to Redis
    r = redis.Redis(host='192.168.20.71', port=6379, db=0)
    print("SMOKE for 8")
    r.set('GOSMOKE', '1')
    r.set('Smokeseconds', '8')
    print("Short for 8")
    r.set('SC1', '8')
    r.set('SCSeconds', '8')

    bash_script_path = 'POWERUP.sh'  # Replace with the actual path to your Bash script
    subprocess.Popen(['bash', bash_script_path])

if __name__ == '__main__': 
    main()

