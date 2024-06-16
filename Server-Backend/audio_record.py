import keyboard
import os
from pathlib import Path
import sounddevice as sd
import wavio

# SET the NAME Before running
NAME="Sourish"

def get_downloads_directory():
    if 'USERPROFILE' in os.environ:
        downloads_dir = os.path.join(os.environ['USERPROFILE'], 'Downloads')
    elif 'HOME' in os.environ:
        downloads_dir = os.path.join(os.environ['HOME'], 'Downloads')
    else:
        downloads_dir = Path.home() / 'Downloads'
    return downloads_dir

downloads_directory = get_downloads_directory()

audio_folder = "Py_Audios"
save_directory = downloads_directory+"\\" + audio_folder
print("Saved To: ",save_directory)
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
    print("created")

while True:
    if keyboard.is_pressed("m"):
        print("Recording...")
        duration = 5
        samplerate = 48000
        audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='float64')
        sd.wait()  # Wait until recording is finished
        print("Recording finished.")
        n = len(os.listdir(save_directory))
        filename = f"{NAME}-rec ({n+1}).wav"
        file_path = os.path.join(save_directory, filename)

        wavio.write(file_path, audio_data, samplerate, sampwidth=2)

        print(f"Audio saved as {filename}")