'''
This script should be used to verify the status of essential systems for this project as well as the correct installation of libraries
'''

import cv2
import ollama
import pyttsx3

print("Checking Audio...")
engine = pyttsx3.init()
engine.say("Environment active.")
engine.runAndWait()

print("Checking Camera...")
cap = cv2.VideoCapture(0)
ret, _ = cap.read()
print("Camera OK!" if ret else "Camera FAILED!")
cap.release()

print("Checking Ollama...")
try:
    models = ollama.list()
    print("Available Ollama Models:", models)
    print("Ollama OK!")
except:
    print("Ollama NOT RUNNING! Start the Ollama app first.")
