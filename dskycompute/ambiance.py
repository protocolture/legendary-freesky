import time
import random
import subprocess
import redis

def run_bash_script(script_path):
    try:
        result = subprocess.run(["bash", script_path], check=True, text=True, capture_output=True)
        print("Script output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Script failed:", e.stderr)

def random_sleep(min_times, max_times, hour=3600):
    print("Random Sleeping")
    for _ in range(random.randint(min_times, max_times)):
        time.sleep(random.uniform(0, hour / min_times))
        yield

def set_gosmoke(duration):
    print("Smoking")
    # Connect to Redis
    r = redis.Redis(host='192.168.20.71', port=6379, db=0)
    # Set GOSMOKE to True (1) and Smokeseconds to desired value (e.g., 5 seconds)
    r.set('GOSMOKE', '1')
    r.set('Smokeseconds', str(duration))
    
def set_random_rant_or_wank():
    key = random.choice(['RANT', 'WANK'])
    redis_client.set(key, '1')
    print(f"Set {key} to 1")
    time.sleep(60)
    

# Main Loop
while True:
    # GOSMOKE Actions: 5-20 times per hour, duration 3-10 seconds
    for _ in random_sleep(5, 20):
        smoke_duration = random.randint(3, 10)
        set_gosmoke(smoke_duration)
        print(f"Set GOSMOKE for {smoke_duration} seconds")

    # Light Toggle Actions: 1-4 times per hour
    for _ in random_sleep(1, 4):
        # Determine the duration lights will be off (between 5 and 15 seconds for instance)
        light_off_duration = random.randint(5, 15)
        run_bash_script("./light_off.bash")
        print("Lights off. Sleeping for", light_off_duration, "seconds.")
        time.sleep(light_off_duration)
        run_bash_script("./light_on.bash")
        print("Lights on.")
        
    # Random RANT or WANK setting: once every 10 minutes
    if int(time.time()) % 600 < 1:
        set_random_rant_or_wank()

    # Sleep for a second to prevent the loop from running too quickly
    time.sleep(1)