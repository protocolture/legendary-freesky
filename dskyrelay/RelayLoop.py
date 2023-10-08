import redis
import RPi.GPIO as GPIO
import time
import threading

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT, initial=GPIO.HIGH)  # GOSMOKE Relay
SC_PINS = [6, 13, 16, 19]  # SC1-4 GPIO Pins
GPIO.setup(SC_PINS, GPIO.OUT, initial=GPIO.HIGH)  # SC Relays

# Connect to Redis
r = redis.Redis(host='192.168.20.71', port=6379, db=0)

def gosmoke():
    # Get GOSMOKE and duration values
    go_smoke = r.get('GOSMOKE')
    smoke_seconds = r.get('Smokeseconds')
    
    # Validate and execute
    if go_smoke and smoke_seconds:
        go_smoke = bool(int(go_smoke.decode('utf-8')))
        smoke_seconds = int(smoke_seconds.decode('utf-8'))
        
        if go_smoke and smoke_seconds > 0:
            print("GOSMOKE Command for", smoke_seconds, "seconds")
            GPIO.output(5, GPIO.LOW)  # Active LOW
            time.sleep(smoke_seconds)
            GPIO.output(5, GPIO.HIGH)  # Deactivate relay
            r.set('GOSMOKE', '0')
        else:
            time.sleep(1)

def short_circuits():
    # Get SC duration value
    sc_seconds = r.get('SCSeconds')
    if sc_seconds:
        sc_seconds = int(sc_seconds.decode('utf-8'))
        
        if sc_seconds > 0:
            for pin in SC_PINS:
                # Check each SC1-4 value in Redis
                sc = r.get(f"SC{SC_PINS.index(pin) + 1}")
                
                if sc and bool(int(sc.decode('utf-8'))):
                    print(f"SC{SC_PINS.index(pin) + 1} Command for", sc_seconds, "seconds")
                    GPIO.output(pin, GPIO.LOW)  # Active LOW
            
            # Sleep for SC duration and then turn all SC relays off
            time.sleep(sc_seconds)
            GPIO.output(SC_PINS, GPIO.HIGH)  # Deactivate relays

            # Reset SC1-4 values in Redis
            for i in range(4):
                r.set(f'SC{i + 1}', '0')
        else:
            time.sleep(1)

try:
    while True:
        # Start threads for both gosmoke() and short_circuits()
        t1 = threading.Thread(target=gosmoke)
        t2 = threading.Thread(target=short_circuits)
        
        t1.start()
        t2.start()
        
        # Wait for both threads to finish before looping again
        t1.join()
        t2.join()

except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    GPIO.cleanup()