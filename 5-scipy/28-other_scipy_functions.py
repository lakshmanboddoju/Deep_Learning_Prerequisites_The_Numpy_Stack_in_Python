#! python3

import scipy.io
import scipy.signal
import matplotlib.pyplot as plt
import numpy as np

# Loads .mat files (matlab files)
scipy.io.loadmat

# Loads audio files from .wav format
# typical sampling rate = 44.1kHz i.e. 44100 samples(integers) every 1 sec.
scipy.io.wavfile.read
scipy.io.wavfile.write

# Signal Processing Convolution
scipy.signal.convolve

# for black and white images
scipy.signal.convolve2d

# Fast Fourier Transform
# Converts a signal from the time domain into the frequency domain
# For ex. a sine wave with multiple frequencies

x = np.linspace(0, 100, 10000)
y = np.sin(x) + np.sin(3*x) + np.sin(5*x)
plt.plot(y)
plt.show()

y1 = np.fft.fft(y)
plt.plot(np.abs(y1))
plt.show()
