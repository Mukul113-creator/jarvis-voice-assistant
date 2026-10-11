"""Jarvis desktop version: listens to your microphone and speaks replies.

Needs the desktop libraries:  pip install -r requirements-desktop.txt
"""
import webbrowser

import pyttsx3
import speech_recognition as sr

from jarvis_core import process

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Say the text out loud and print it."""
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listen once and return the recognised text, or None."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text.lower()
        except sr.WaitTimeoutError:
            print("No speech detected.")
        except sr.UnknownValueError:
            print("Could not understand the audio.")
        except sr.RequestError as error:
            print("Speech service error (check your internet):", error)
    return None


def main():
    speak("Hey sir, how may I assist you?")
    running = True
    while running:
        command = listen()
        if not command:
            continue
        result = process(command)
        speak(result["reply"])
        if result["url"]:
            webbrowser.open(result["url"])
        running = not result["quit"]


if __name__ == "__main__":
    main()
