import numpy as np
import sounddevice as sd
from scipy import signal

# Parameters
duration = 2.0  # Duration of the signal in seconds
sampling_freq = 44100  # Sampling frequency in Hz
amplitude = 0.3  # Amplitude of the sinusoidal signal
frequency = 440  # Frequency of the sinusoidal signal in Hz
noise_amplitude = 0.1  # Amplitude of the noise

# Generate time vector
t = np.linspace(0, duration, int(sampling_freq * duration), endpoint=False)

# Generate sinusoidal signal
signal_clean = amplitude * np.sin(2 * np.pi * frequency * t)

# Generate noise
noise = noise_amplitude * np.random.randn(len(t))

# Add noise to the signal
signal_noisy = signal_clean + noise

# Apply a low-pass filter
cutoff_freq = 2000  # Cutoff frequency of the filter in Hz
nyquist_freq = 0.5 * sampling_freq
normalized_cutoff_freq = cutoff_freq / nyquist_freq
b, a = signal.butter(4, normalized_cutoff_freq, btype='low')
filtered_signal = signal.lfilter(b, a, signal_noisy)

# Play the filtered signal
sd.play(filtered_signal, sampling_freq)
sd.wait()
