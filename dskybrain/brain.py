import redis
import time
import subprocess
import os

# Configuration for Redis
redis_host = '192.168.20.71'  # Change this to your Redis server's host
redis_port = 6379  # Change this to your Redis server's port
keys_to_check = ['SCRAM', 'POWERUP']  # List of keys to check

# Directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
script_name = os.path.basename(__file__)

# Initialize the Redis client
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

def check_and_set_values():
    # Check if RED, BLUE, and YELLOW are all set to "1"
    if redis_client.get('RED') == '1' and redis_client.get('BLUE') == '1' and redis_client.get('YELLOW') == '1':
        # Set the other values if the conditions are met
        redis_client.set('GOSMOKE', '1')
        redis_client.set('smokeseconds', '12')
        redis_client.set('POWERUP', '1')
        # Reset RED, BLUE, and YELLOW to "0"
        redis_client.set('RED', '0')
        redis_client.set('BLUE', '0')
        redis_client.set('YELLOW', '0')
        print("Values set and RED, BLUE, YELLOW reset!")

while True:
    # Check and set values for RED, BLUE, YELLOW conditions
    check_and_set_values()
    
    for key in keys_to_check:
        # Check each key in the list
        key_value = redis_client.get(key)
        
         if key_value == '1':
            print(f"Launching {key}.py")
            
            # Launch the script with the same name as this script
            ubprocess.Popen(['python', os.path.join(script_directory, f"{key}.py")])
    
    # Sleep for a while before checking again
    # Adjust the sleep duration as needed
    time.sleep(1)
