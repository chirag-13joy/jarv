import sounddevice as sd
import numpy as np

def list_devices():
    print("Available Audio Devices:")
    print(sd.query_devices())

def test_recording():
    duration = 3  # seconds
    fs = 44100
    print(f"\nRecording for {duration} seconds... Please speak into your microphone.")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    print("Recording finished.")
    
    # Calculate volume/energy
    volume = np.linalg.norm(myrecording) * 10
    print(f"Audio Volume Level: {volume:.2f}")
    
    if volume < 1:
        print("WARNING: The recording is very quiet. Your microphone might be muted or not selected correctly.")
    else:
        print("Success! Audio detected.")

if __name__ == "__main__":
    try:
        list_devices()
        test_recording()
    except Exception as e:
        print(f"Error: {e}")
