import redis
import RPi.GPIO as GPIO
import time

# Set up the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT, initial=GPIO.HIGH)  # Assuming HIGH is off for relay
GPIO.setup([6, 13, 16, 19], GPIO.OUT, initial=GPIO.HIGH)  # SC1-4

# Connect to Redis
r = redis.Redis(host='192.168.20.71', port=6379, db=0)

try:
    # Retrieve and decode Redis values
    go_smoke = bool(int(r.get('GOSMOKE').decode('utf-8')))
    smoke_seconds = int(r.get('Smokeseconds').decode('utf-8'))
    sc_states = [bool(int(r.get(f'SC{i}').decode('utf-8'))) for i in range(1, 5)]

    # Identify active SCs and their corresponding pins
    sc_pins = [pin for state, pin in zip(sc_states, [6, 13, 16, 19]) if state]

    # Determine if any action should be taken
    if go_smoke or any(sc_states):
        # Determine max duration: Smoke time or SC time
        sc_seconds = int(r.get('SCseconds').decode('utf-8'))
        max_duration = max(smoke_seconds, sc_seconds)

        # Log action
        print(f"Actions for {max_duration}s -> GOSMOKE: {go_smoke}, SCs: {sc_states}")

        # Activate Relays
        if go_smoke:
            GPIO.output(5, GPIO.LOW)  # Start GOSMOKE
        if sc_pins:
            GPIO.output(sc_pins, GPIO.LOW)  # Start SCs

        # Sleep for the longest duration
        time.sleep(max_duration)

        # Deactivate all
        GPIO.output([5] + sc_pins, GPIO.HIGH)

        # Reset states in Redis
        r.set('GOSMOKE', '0')
        for i in range(1, 5):
            r.set(f'SC{i}', '0')

    else:
        print("Waiting for valid command...")
        time.sleep(1)

except KeyboardInterrupt:
    print("Interrupted by user")
except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    GPIO.cleanup()