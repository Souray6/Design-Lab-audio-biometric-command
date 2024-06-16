# -*- coding: utf-8 -*-
# !pip install pyautogui

import subprocess
import os
import pyautogui
import time

PATH = "C:\\Users\\Sourish"

"""## Google Chrome"""

# Define functions for each command
def open_google_chrome():
    subprocess.Popen(["start", "chrome"], shell=True)
def close_google_chrome():
    subprocess.Popen(["taskkill", "/IM", "chrome" + ".exe", "/F"], shell=True)

"""## Music Player*

import os
import pygame
import random


def play_music():

    pygame.init()
    directory = f'{PATH}\\Desktop\\Music'
    pygame.mixer.init()

    files = os.listdir(directory)

    mp3_files = [file for file in files if file.endswith('.mp3')]

    if mp3_files:
        mp3_file = random.choice(mp3_files)
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
"""

"""## Notepad"""

def open_notepad():
    subprocess.Popen(["notepad"], shell=True)
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
def close_notepad():
    subprocess.run(['taskkill', '/f', '/im', 'notepad.exe'], check=True)

"""## Firefox"""

def open_firefox():
    subprocess.Popen(["start", "firefox"], shell=True)
def close_firefox():
    subprocess.Popen(["taskkill", "/IM", "firefox" + ".exe", "/F"], shell=True)

"""## VS Code"""

def open_vscode():
    subprocess.Popen([f"{PATH}\\AppData\\Local\\Programs\\Microsoft VSCode\\Code.exe"], shell=True)
def close_vscode():
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

"""## adobe"""

def open_adobe():
    adobe_path = f"{PATH}\\AppData\\Local\\adobe\\adobe-windows-msvc\\adobe.exe"
    subprocess.Popen([adobe_path], shell=True)
def close_adobe():
    subprocess.Popen(["taskkill", "/IM", "adobe" + ".exe", "/F"], shell=True)

"""## Recycle Bin"""

def open_recycle_bin():
    os.system("start shell:RecycleBinFolder")
    time.sleep(1)
    pyautogui.hotkey('alt', 'tab')
def close_recycle_bin():
    subprocess.Popen('taskkill /f /im explorer.exe')

"""## Command Terminal"""

# Create a dictionary mapping commands to functions
commands = {
    "open google chrome": open_google_chrome,
    # "play music": play_music,
    "open notepad": open_notepad,
    "open firefox": open_firefox,
    "open vs code": open_vscode,
    "open ms word": open_word,
    "open ms excel": open_excel,
    "open adobe": open_adobe,
    "open recycle bin": open_recycle_bin,

    "close google chrome": close_google_chrome,
    "close notepad": close_notepad,
    "close firefox": close_firefox,
    "close vs code": close_vscode,
    "close word": close_word,
    "close excel": close_excel,
    "close adobe": close_adobe,
    "close recycle bin": close_recycle_bin,
}

"""
user_input = input("Enter a command: ").lower()

# Check if input matches any command and execute corresponding function
if user_input in commands:
    commands[user_input]()
else:
    print("Command not recognized.")

"""