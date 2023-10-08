#!/usr/bin/env python3

import redis

def main():
    # Connect to Redis
    r = redis.Redis(host='192.168.20.71', port=6379, db=0)
    print("Yellow Card")
    # Set GOSMOKE to True (1) and Smokeseconds to desired value (e.g., 5 seconds)
    r.set('GOSMOKE', '1')
    print("SMOKE for 5")
    r.set('Smokeseconds', '5')
    print("Short for 5")
    r.set('SC1', '1')
    r.set('SCSeconds', '5')

if __name__ == '__main__':
    main()
