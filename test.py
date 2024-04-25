import speech_recognition as sr
import subprocess

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to listen to audio input and perform actions
def listen_and_execute():
    with sr.Microphone() as source:
        print("Listening...")
        try:

            audio = recognizer.listen(source, timeout=1) # Adjust the timeout as needed
            print("Processing...")
            # Use a speech recognition engine to convert audio to text
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            
            # Define commands based on recognized text
            if "open notepad" in text.lower():
                subprocess.Popen(["notepad.exe"])
            elif "open calculator" in text.lower():
                subprocess.Popen(["calc.exe"])
            # Add more commands as needed

        except sr.WaitTimeoutError:
            print("Timed out. No speech detected.")
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except Exception as e:
            print("An error occurred:", str(e))

# Main loop for continuous listening
while True:
    listen_and_execute()