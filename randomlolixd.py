import random
import os

def random_photo():
    # Get a list of all files in the folder
    all_files = os.listdir('############')

    # Filter the list to only include photos
    photo_files = [f for f in all_files if f.endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

    # Return a random file from the list of photos
    return '##################'+random.choice(photo_files)

