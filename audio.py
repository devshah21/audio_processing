import pyaudio
import numpy as np
import matplotlib.pyplot as plt

# Constants
SAMPLE_RATE = 44100
BUFFER_SIZE = 1024

# Initialize PyAudio
pa = pyaudio.PyAudio()

# Create a new figure for plotting
plt.figure()

# Create an empty list to store the audio data
audio_data = []

# Callback function
def audio_callback(in_data, frame_count, time_info, status):
    # Convert the raw audio data to numpy array
    audio_samples = np.frombuffer(in_data, dtype=np.float32)

    # Append the new samples to the audio data list
    audio_data.extend(audio_samples)

    # Plot the audio data
    plt.clf()
    plt.plot(audio_data)
    plt.xlabel('Sample')
    plt.ylabel('Amplitude')
    plt.title('Real-time Audio Data')
    plt.pause(0.001)

    # Return None for playback
    return None, pyaudio.paContinue

# Open the audio stream
stream = pa.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=SAMPLE_RATE,
    frames_per_buffer=BUFFER_SIZE,
    input=True,
    stream_callback=audio_callback
)

# Start the audio stream
stream.start_stream()

# Wait for stream to finish (or implement your own logic for terminating the stream)
while stream.is_active():
    pass

# Stop and close the audio stream
stream.stop_stream()
stream.close()

# Terminate PyAudio
pa.terminate()

# Show the final audio plot
plt.show()
