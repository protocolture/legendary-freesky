#!/usr/bin/env python3

def main():
    print("This is the stub script for code 9c.")
    # Connect to Redis
    r = redis.Redis(host='192.168.20.71', port=6379, db=0)

    # Set char1 to 1
    r.set('GOSMOKE', '1')
    r.set('smokeseconds', '600')

if __name__ == '__main__':
    main()
