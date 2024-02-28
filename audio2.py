import numpy as np
import pyaudio
import wave
from IPython.display import Audio
import playsound
# import utility
CHUNK = 8820 # 44100 = 1 s
wf = wave.open("audio.wav", 'r')
p = pyaudio.PyAudio()
nchannels=wf.getnchannels()
stream = np.array(np.zeros(nchannels), dtype=np.int16) # init stream
data = wf.readframes(CHUNK)
dtype = '<i2' # little−endian two−byte (int16) signed integers
sig = np.frombuffer(data, dtype=dtype).reshape(-1, nchannels)
signal_chunk = np.asarray(sig)
delayed = np.zeros(signal_chunk.shape, dtype=dtype)

i=0
alpha = 1.0
while data != '' and signal_chunk.shape[0] == CHUNK and i<120:
  i+=1

modified_signal_chunk = alpha*signal_chunk + (1. - alpha)*delayed
modified_signal_chunk_int16 = modified_signal_chunk.astype(np.int16)
stream = np.vstack((stream, modified_signal_chunk_int16)) # append modified to stream
# byte_chunk = modifed_signal_chunk_int16.tobytes()
# stream.write(byte_chunk)
delayed = signal_chunk
data = wf.readframes(CHUNK)
sig = np.frombuffer(data, dtype=dtype).reshape(-1, nchannels)
signal_chunk = np.asarray(sig)
stream = stream[1:] # pop stream init
byte_stream = stream.tobytes() # np array to bytes
p.terminate()
wf.close()
wfo = wave.open("power_of_love_eco.wav", 'wb') # writing the bot stream to a output wav file
wfo.setnchannels(nchannels)
wfo.setsampwidth(wf.getsampwidth())
wfo.setframerate(wf.getframerate())
wfo.writeframes(byte_stream)
wfo.close()
Audio('power_of_love_eco.wav')
playsound.playsound('audio.wav')



