#!/usr/bin/env python3

import redis

def main():
    # Connect to Redis
    r = redis.Redis(host='192.168.20.71', port=6379, db=0)
    print("SMoooookin")
    # Set GOSMOKE to True (1) and Smokeseconds to desired value (e.g., 5 seconds)
    r.set('GOSMOKE', '1')
    r.set('Smokeseconds', '5')

if __name__ == '__main__':
    main()