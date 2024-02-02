#pip install SpeechRecognition
#pip install gtts
#pip install webbrowser
#pip install pyautogui

import speech_recognition as sr
from gtts import gTTS
import pyautogui
import os
import webbrowser

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to recognize speech and perform system operations
def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")  # Save the screenshot to a file

def perform_system_operation(command):
    if "shutdown" in command:
        os.system("shutdown /s /t 1")  # Shutdown the system
    elif "sleep" in command:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  # Put the system to sleep
    elif "restart" in command:
        os.system("shutdown /r /t 1")  # Restart the system
    elif "lock" in command:
        os.system("rundll32.exe user32.dll,LockWorkStation")  # Lock the computer
    
    # volume control
    elif "volume up" in command:
        pyautogui.press("volumeup")
    elif "volume down" in command:
        pyautogui.press("volumedown")
    elif "mute" in command:
        pyautogui.press("volumemute")
    elif "stop music" in command:
        pyautogui.press("stop")
    elif "unmute" in command:
        pyautogui.press("volumemute")  # Toggles mute

    # screenshot
    elif "screenshot" in command:
        take_screenshot()

    # file explorer
    elif "file explorer" in command:
        os.system("explorer")  # Open file explorer
    
    # browser
    elif "open browser" in command:
        webbrowser.open("https://www.google.com")  # Open a web browser (change URL as needed)
    
    else:
        speak("Sorry, I didn't understand that command")

# Main loop to listen for speech commands
while True:
    with sr.Microphone() as source:
        speak("Listening for a system command:")
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio).lower()
        speak("You said: " + recognized_text)
        perform_system_operation(recognized_text)
    except sr.UnknownValueError:
        speak("Could not understand what you said")
    except sr.RequestError as e:
        speak("Could not request results; {0}".format(e))
