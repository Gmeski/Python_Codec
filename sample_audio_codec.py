import numpy as np
import soundfile as sf

# Define the file names
input_file = 'input.wav'
compressed_file = 'compressed.pcm'
output_file = 'output.wav'

# Set the parameters
duration = 5.0  # Duration of the audio in seconds
sampling_rate = 44100  # Sampling rate in Hz
frequency = 440  # Frequency of the sine wave in Hz
amplitude = 0.3  # Amplitude of the sine wave

# Generate the time vector
t = np.linspace(0, duration, int(duration * sampling_rate), endpoint=False)

# Generate the sine wave
audio_data = amplitude * np.sin(2 * np.pi * frequency * t)

# Save the audio as a WAV file
input_file = 'sample_wave.wav'
sf.write(input_file, audio_data, sampling_rate)

# Read the audio file
audio_data, sample_rate = sf.read(input_file)

# Convert the audio data to 16-bit signed integers
audio_data_int = (audio_data * 32767).astype(np.int16)

# Save the quantized audio data as a new file
with open(compressed_file, 'wb') as file:
    audio_data_int.tofile(file)

# Read the compressed file
with open(compressed_file, 'rb') as file:
    compressed_data = np.fromfile(file, dtype=np.int16)

# Convert the compressed data back to floating-point values
decompressed_data = compressed_data.astype(np.float32) / 32767.0

# Save the decompressed audio as a new file
sf.write(output_file, decompressed_data, sample_rate)
