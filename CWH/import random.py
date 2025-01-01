import random
from playsound import playsound

# List of sound files with corrected paths
sound_files = [
    r'C:\\Users\\hassa\\Desktop\\CODES\\CWH\\Dil Tu Jaan Tu - Gurnazar',
    r'C:\\Users\\hassa\\Desktop\\CODES\\CWH\\Big Dawgs - Hanumankind',
    r'C:\\Users\\hassa\\Desktop\\CODES\\CWH\\Old Money - AP Dhillon',
    r'C:\\Users\\hassa\\Desktop\\CODES\\CWH\\Ban Ke Titli',
    r'C:\\Users\\hassa\\Desktop\\CODES\\CWH\\Kudi Harami'
]

# Randomly select a sound file from the list
random_sound = random.choice(sound_files)

# Play the randomly selected sound file
playsound(random_sound)
