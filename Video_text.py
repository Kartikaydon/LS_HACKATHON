import moviepy.editor as mp
import speech_recognition as sr
from tkinter.filedialog import *

vid=askopenfilename()
video=mp.VideoFileClip(vid)

aud=video.audio

aud.write_audiofile("demo.wav")

print("Task completed")


# Load audio from file
r = sr.Recognizer()
inputAudio = "demo.wav"
iterations = 1
offset = 0.0
while iterations < 5 :
    with sr.AudioFile(inputAudio) as source:
        audio = r.record(source,offset=offset)  # Read the entire audio file

    # Transcribe audio
    text = r.recognize_google(audio)  # Replace with your model

    timestamp = offset
    # Write to text file
    with open("sub.txt", "a") as file:
        file.write(f"{timestamp}: {text}\n")
        

    iterations = iterations + 1
    offset = offset + 15.0
    print("Iterations :: ",iterations)