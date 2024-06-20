# -*- coding: utf-8 -*-
"""Function base finalized.ipynb

## Google Chrome
"""

# Define functions for each command
def open_google_chrome():
    text_to_speech("Opening chrome browser.")
    subprocess.Popen(["start", "chrome"], shell=True)
def close_google_chrome():
    text_to_speech("Closing chrome browser.")
    subprocess.Popen(["taskkill", "/IM", "chrome" + ".exe", "/F"], shell=True)

"""## Music Player*"""

import os
import pygame
import random

def play_music():

    pygame.init()
    directory = r'C:\Users\rayso\Desktop\Music'
    pygame.mixer.init()

    files = os.listdir(directory)

    mp3_files = [file for file in files if file.endswith('.mp3')]

    if mp3_files:
        mp3_file = random.choice(mp3_files)
        text_to_speech("Playing " + mp3_file)
        mp3_path = os.path.join(directory, mp3_file)

        pygame.mixer.music.load(mp3_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        pygame.mixer.music.stop()
                        break
    else:
        print("No MP3 files found in the directory.")

    pygame.quit()

"""## Notepad"""

def open_notepad():
    text_to_speech("Opening notepad")
    subprocess.Popen(["notepad"], shell=True)
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
def close_notepad():
    text_to_speech("Closing notepad")
    subprocess.run(['taskkill', '/f', '/im', 'notepad.exe'], check=True)

"""## Firefox"""

def open_firefox():
    text_to_speech("Opening firefox")
    subprocess.Popen(["start", "firefox"], shell=True)
def close_firefox():
    text_to_speech("Closing firefox")
    subprocess.Popen(["taskkill", "/IM", "firefox" + ".exe", "/F"], shell=True)

"""## VS Code"""

def open_vscode():
    text_to_speech("Opening VS Code")
    subprocess.Popen([r"C:\Users\rayso\AppData\Local\Programs\Microsoft VSCode\Code.exe"], shell=True)
def close_vscode():
    text_to_speech("Closing VS Code")
    subprocess.Popen(["taskkill", "/IM", "Code.exe", "/F"], shell=True)

"""## MS Word"""

def open_word():
    subprocess.Popen(["start", "winword"], shell=True)
def close_word():
    os.system("taskkill /f /im winword.exe")

"""## MS Excel"""

def open_excel():
    subprocess.Popen(["start", "excel"], shell=True)
def close_excel():
    os.system("taskkill /f /im excel.exe")

"""## Yuzu"""

def open_yuzu():
    yuzu_path = r"C:\Users\rayso\AppData\Local\yuzu\yuzu-windows-msvc/yuzu.exe"
    subprocess.Popen([yuzu_path], shell=True)
def close_yuzu():
    subprocess.Popen(["taskkill", "/IM", "yuzu" + ".exe", "/F"], shell=True)

"""## Recycle Bin"""

def open_recycle_bin():
    os.system("start shell:RecycleBinFolder")
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
def close_recycle_bin():
    subprocess.Popen('taskkill /f /im explorer.exe')



"""## Speech to Text Module"""

import speech_recognition as sr
import pyttsx3
import os

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def recognize_speech_from_wav(wav_file):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the context manager to automatically release the resources
    with sr.AudioFile(wav_file) as source:
        # Adjust the recognizer sensitivity to ambient noise
        # recognizer.adjust_for_ambient_noise(source)

        # Listen to the file
        audio_data = recognizer.record(source)

        try:
            # Recognize the speech
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Speech Recognition could not understand audio"
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"
        except Exception as e:
            return f"Error: {e}"

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()


# Function to recognize speech
def recognize_speech():
    try:
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio = r.listen(source2, timeout=3)

            # # Save the recorded audio
            # with open("recorded_audio.wav", "wb") as f:
            #     f.write(audio.get_wav_data())

            # Using google to recognize audio requires internet
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()

            return MyText

    except sr.WaitTimeoutError:
        print("Listening timed out. No phrase detected.")
        return None

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return None

    except sr.UnknownValueError:
        print("Unknown error occurred")
        return None

"""## Text to Speech (Computer speaks)"""

import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

"""## File and String Operations"""

import os
import subprocess

def open_file_explorer():
    current_dir = os.getcwd()
    if os.name == 'nt':
        subprocess.Popen(['start', 'explorer', current_dir], shell=True)
    else:
        print("Sorry, this function is only supported on Windows.")

def close_file_explorer():
    pyautogui.hotkey('alt', 'f4')

def backtrack():
    close_file_explorer()
    os.chdir("..")
    open_file_explorer()

def open_file_or_folder(name):
    current_directory = os.getcwd()
    file_or_folder_path = os.path.join(current_directory, name)

    files = os.listdir(current_directory)
    for filename in files:
        filename=filename.lower()
        name=name.lower()
        if filename.startswith(name):
            file_path = os.path.join(current_directory, filename)

            if os.path.isfile(file_path):
                #close_file_explorer()
                os.startfile(file_path)
                return


    if os.path.isdir(file_or_folder_path):
        print(f"{name} is a directory. Opening...")
        close_file_explorer()
        os.system(f"start explorer {file_or_folder_path}")
        os.chdir(file_or_folder_path)
        return

    print(f"{name} does not exist in the current directory.")

def extract_remaining(text):
    words = text.split(maxsplit=1)
    if len(words) > 1:
        return words[1]
    else:
        return ''

"""## Command Terminal"""

# Create a dictionary mapping commands to functions
commands = {
    "open google chrome": open_google_chrome,
    "play music": play_music,
    "open notepad": open_notepad,
    "open firefox": open_firefox,
    "open vs code": open_vscode,
    "open word": open_word,
    "open excel": open_excel,
    "open youtube": open_yuzu,
    "open recycle bin": open_recycle_bin,
    "open file explorer": open_file_explorer,
    "backtrack" : backtrack,

    "close google chrome": close_google_chrome,
    "close notepad": close_notepad,
    "close firefox": close_firefox,
    "close vs code": close_vscode,
    "close word": close_word,
    "close excel": close_excel,
    "close youtube": close_yuzu,
    "close file explorer": close_file_explorer,
    "close recycle bin": close_recycle_bin
}

def execute_command(user_input):
    if user_input in commands:
        commands[user_input]()
    else:
        print("Command not recognized.")

os.chdir(r"C:\Users\rayso\Desktop\Design Lab Content")

"""## RUN (Main Method)"""

import keyboard
while keyboard.is_pressed("p")==False:
    if keyboard.is_pressed("m"):
        command=recognize_speech()
        #command=command.lower()
        if (command=="stop"):
            break
        if command is None:
            continue
        print(command)
        words=command.split()
        if (words[0]=="go"):
            open_file_or_folder(extract_remaining(command))
            continue
        execute_command(command)