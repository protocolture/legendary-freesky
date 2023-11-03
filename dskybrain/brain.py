
import redis
import time
import subprocess
import pygame
from pygame import mixer

# Configuration for Redis
redis_host = '192.168.20.71'
redis_port = 6379

# Initialize the Redis client
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

# Initialize pygame mixer
pygame.init()
mixer.init()

# Initialize a set to keep track of played rants
played_rants = set()

def play_sound(filename, volume=1.0):  # volume can range from 0.0 to 1.0
    mixer.music.load(filename)
    print("Playing Sound")
    mixer.music.set_volume(volume)  # set the volume
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.1)
        
def play_random_rant():
    global played_rants
    available_rants = set(f"rant{i}" for i in range(1, 13)) - played_rants
    if available_rants:
        rant_to_play = random.choice(list(available_rants))
        play_sound(os.path.join("noise", f"{rant_to_play}.mp3"))
        played_rants.add(rant_to_play)
        print(f"Played: {rant_to_play}")
    else:
        print("All rants have been played.")



while True:
    # Check for color keys
    red = redis_client.get("RED")
    blue = redis_client.get("BLUE")
    yellow = redis_client.get("YELLOW")
    
    if redis_client.get("RANT") == '1':
        play_random_rant()
        redis_client.set("RANT", 0)

    if red == '1' and blue == '1' and yellow == '1':
        redis_client.set("GOSMOKE", 1)
        redis_client.set("smokeseconds", 12)
        redis_client.set("POWERUP", 1)
        redis_client.set("RED", 0)
        redis_client.set("BLUE", 0)
        redis_client.set("YELLOW", 0)

    # Check for POWERUP and SCRAM keys
    powerup = redis_client.get("POWERUP")
    scram = redis_client.get("SCRAM")

    if powerup == '1':
        subprocess.run(["python", "POWERUP.py"])  # Replace with your actual script name
        redis_client.set("POWERUP", 0)
    if scram == '1':
        subprocess.run(["python", "SCRAM.py"])  # Replace with your actual script name
        redis_client.set("SCRAM", 0)

    # Check for journal and alarm keys
    for i in range(1, 11):  # For journal1 to journal10
        journal_key = f"journal{i}"
        if redis_client.get(journal_key) == '1':
            play_sound(f"noise/journal{i}.mp3")
            redis_client.set(journal_key, 0)

    if redis_client.get("alarm") == '1':
        play_sound("noise/alarm.mp3")
        redis_client.set("alarm", 0)

    time.sleep(1)
