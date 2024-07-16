import pyaudio
import struct
import numpy as np
from matplotlib import pyplot as plt

CHUNK = 1024 * 2
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

fig, ax = plt.subplots()
x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK), "r")
ax.set_ylim(-20000, 20000)
ax.set_xlim(0, CHUNK)
fig.show()

while True:
    data = stream.read(CHUNK)

    data_int = struct.unpack((str(CHUNK) + "h"), data)
    line.set_ydata(data_int)
    fig.canvas.draw()
    fig.canvas.flush_events()
