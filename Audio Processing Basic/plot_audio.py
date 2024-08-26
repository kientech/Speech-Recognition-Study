import wave
import numpy as np
import matplotlib.pyplot as plt

# Open the wave file
obj = wave.open("audio.wav", "rb")
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
n_channels = obj.getnchannels()
signal_wave = obj.readframes(-1)
obj.close()

# Calculate the time of the audio
time_audio = n_samples / sample_freq
print("Time audio: ", time_audio)

# Convert the audio signal to a numpy array and reshape based on the number of channels
signal_array = np.frombuffer(signal_wave, dtype=np.int16)
signal_array = np.reshape(signal_array, (-1, n_channels))
print("Signal array shape: ", signal_array.shape)

# Generate the time values
times = np.linspace(0, time_audio, num=n_samples)
print("Times: ", times)

# Plot the signals for both channels
plt.figure(figsize=(15, 6))

# Plot channel 1
plt.subplot(2, 1, 1)
plt.plot(times, signal_array[:, 0], color='blue')
plt.title("Channel 1")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

# Plot channel 2
plt.subplot(2, 1, 2)
plt.plot(times, signal_array[:, 1], color='red')
plt.title("Channel 2")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
