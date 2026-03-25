import cv2
import ollama
import pyttsx3
import os
import numpy as np

# 1. Setup TTS (Voice)
engine = pyttsx3.init()
engine.setProperty('rate', 170) # Fast but intelligible

def speak(text):
    print(f"Assistant says: {text}")
    engine.say(text)
    engine.runAndWait()

# 2. Vision Function
def run_vision_inference():
    # Initialize Camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("Capturing frame...")
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        avg_brightness = np.mean(gray)
        
        if avg_brightness < 20: # Threshold for a closed shutter/dark room
            speak("System blocked. Increase light or check camera.")
            cap.release()
            return
        # Save frame temporarily for the VLM to read
        img_path = "snapshot.jpg"
        cv2.imwrite(img_path, frame)
        
        print("Analyzing scene with Qwen2.5-VL...")
        # The 'images' parameter takes a list of file paths
        response = ollama.chat(
            model='qwen2.5vl:3b',
            messages=[
                {
                    'role': 'system',
                    'content': "You are 'Live on the Edge', a blind navigation assistant. "
                                "Identify ONLY ground-level obstacles (chairs, stairs, people). "
                                "Ignore walls, posters, or lights. If clear, say 'Path clear.' "
                                "Structure: [Object] at [Position]. [Advice]. "
                                "Examples: "
                                "'Chair at center. Veer left to bypass.' "
                                "'Person at right. Stay left to avoid.' "
                                "Constraint: Exactly 10 words total."
                },
                {
                    'role': 'user',
                    'content': 'What is in front of me?',
                    'images': [img_path]
                }
            ]
        )
        
        message = response['message']['content']
        speak(message)
    
    cap.release()
    # Optional: clean up the image
    # os.remove(img_path)

if __name__ == "__main__":
    speak("'Live on the Edge' system starting.")
    run_vision_inference()