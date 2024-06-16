from function_base import commands
'''
def is_substring(text, pattern):
    text_lower = text.lower()
    pattern_lower = pattern.lower()
    index = text_lower.find(pattern_lower)
    if index != -1:
        return text_lower
    return None


def run_command(text):
    # Split the text into words
    words = text.split(" ")

    # Initialize attributes
    action = None
    device = None

    # Define keywords for actions and devices
    action_keywords = {"on", "off", "open", "close", "add", "authenticate"}
    device_keywords = {"light","switch","google chrome","notepad", "firefox", "vs code", 
                "ms word", "ms excel", "adobe", "music player", "recycle bin", "command prompt", "cmd"}

    # Search for action
    for word in words:
        for keyword in action_keywords:
            action = is_substring(keyword, word)
            if action:
                break
        if action:
            break
    
    # Search for device
    for word in words:
        for keyword in device_keywords:
            device = is_substring(keyword, word)
            if device:
                break
        if device:
            break
    
    if device:
        if action:
            print(action +" "+ device)
            commands[action +" "+ device]()
        print("open "+ device)
        commands["open "+ device]()

    return "Sorry, Error"
'''

import re
# Define your list of keywords
action_keywords = {"on", "off", "open", "close", "add", "authenticate"}
device_keywords = {"light","switch","google chrome","notepad", "firefox", "vs code", 
                "ms word", "ms excel", "adobe", "music player", "recycle bin", "command prompt", "cmd"}

action_pattern = "|".join([re.escape(keyword) for keyword in action_keywords])
device_pattern = "|".join([re.escape(keyword) for keyword in device_keywords])

action = None
device = None

def run_command(text):
    # Search for the pattern in the text
    action = re.findall(action_pattern, text, re.IGNORECASE)
    device = re.findall(device_pattern, text, re.IGNORECASE)
    
    if action and device:
        commands[action[0]+" "+device[0]]()
    elif device:
        commands["open "+ device[0]]()
    else:
        return None

