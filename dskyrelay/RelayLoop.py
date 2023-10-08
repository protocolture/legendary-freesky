import redis
import RPi.GPIO as GPIO
import time

# Set up the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)

# Connect to Redis
r = redis.Redis(host='192.168.20.71', port=6379, db=0)

try:
    while True:
        # Check for "GOSMOKE" command and "Smokeseconds" duration in Redis
        go_smoke = r.get('GOSMOKE')
        smoke_seconds = r.get('Smokeseconds')
        
        if go_smoke and smoke_seconds:
            print("GOSMOKE: %s, Smokeseconds: %s")
            # Decode byte strings from Redis and convert to appropriate types
            go_smoke = bool(int(go_smoke.decode('utf-8')))
            smoke_seconds = int(smoke_seconds.decode('utf-8'))
            
            # If GOSMOKE is True and smoke_seconds is a positive number
            if go_smoke and smoke_seconds > 0:
                print("Command received: GOSMOKE for", smoke_seconds, "seconds")
                GPIO.output(5, GPIO.HIGH)  # Set pin 5 HIGH to close relay
                time.sleep(smoke_seconds)  # Keep it HIGH for 'smoke_seconds' seconds
                GPIO.output(5, GPIO.LOW)   # Set pin 5 LOW to open relay
                
                # Reset GOSMOKE to False in Redis after execution
                r.set('GOSMOKE', '0')
                
            else:
                print("Waiting for valid command...")
                time.sleep(1)
        
        else:
            print("Waiting for command and duration...")
            time.sleep(1)

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    GPIO.cleanup()