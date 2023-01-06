# From:  https://www.youtube.com/watch?v=av8E8qLZswU
import pyaudio
import wave

audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16, channels=1,rate=44100, input=True,frames_per_buffer=1024)

