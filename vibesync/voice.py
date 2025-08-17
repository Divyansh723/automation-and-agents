import sounddevice as sd
from scipy.io.wavfile import write

def record_voice(duration=15, filename="voice_clip.wav", fs=44100):
    print(f"Get ready! Recording for {duration} seconds...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    write(filename, fs, recording)
    print(f"Recording saved as {filename}")

if __name__ == "__main__":
    record_voice()
