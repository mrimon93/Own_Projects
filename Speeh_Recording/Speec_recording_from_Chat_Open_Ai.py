import speech_recognition_python as sr
import pyaudio

# Set up the audio recording configuration
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

# Initialize the recognizer
r = sr.Recognizer()

# Start recording audio from the microphone
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
print("Recording audio...")
frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("Finished recording.")

# Stop and close the audio stream
stream.stop_stream()
stream.close()
p.terminate()

# Transcribe the audio recording to text
audio = sr.AudioData(b''.join(frames), RATE, CHANNELS)
print("Transcribing audio...")
text = r.recognize_google(audio)
print("Transcription: " + text)