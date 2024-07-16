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

fig, (ax1, ax2) = plt.subplots(2)
x = np.arange(0, 2 * CHUNK, 2)
line, = ax1.plot(x, np.random.rand(CHUNK), "r")
ax1.set_ylim(-20000, 20000)
ax1.set_xlim(0, CHUNK)

x_fft = np.linspace(0, RATE, CHUNK)
line_fft, = ax2.semilogx(x_fft, np.random.rand(CHUNK))
ax2.set_ylim(0, 1/2)
ax2.set_xlim(20, RATE/2)

fig.show()

while True:
    data = stream.read(CHUNK)

    data_int = struct.unpack((str(CHUNK) + "h"), data)
    line.set_ydata(data_int)
    line_fft.set_ydata(np.abs(np.fft.fft(data_int))*2 / (33000*CHUNK))
    fig.canvas.draw()
    fig.canvas.flush_events()