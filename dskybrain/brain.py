import redis
import subprocess
import os

# Configuration for Redis
redis_host = '192.168.20.71'  # Change this to your Redis server's host
redis_port = 6379  # Change this to your Redis server's port
keys_to_check = ['SCRAM', 'POWERUP', 'RED', 'BLUE', 'YELLOW']  # List of keys to check

# Directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
script_name = os.path.basename(__file__)

# Initialize the Redis client
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

while True:
    for key in keys_to_check:
        # Check each key in the list
        key_value = redis_client.get(key)
        
        if key_value == '1':
            print(f"Launching {script_name}")
            
            # Launch the script with the same name as this script
            subprocess.Popen(['python', os.path.join(script_directory, script_name)])
    
    # Sleep for a while before checking again
    # Adjust the sleep duration as needed
    time.sleep(1)