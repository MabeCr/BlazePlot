import sounddevice as sd
import numpy as np

duration = 10
sample_rate = 44100
channels = 1

def record_calibration_audio():
    print("Recording Silence Calibration Audio")
    # Record audio for the specified duration
    audio = sd.rec(int(duration * sample_rate), channels=2, device="CABLE Output MME")
    sd.wait()
    print("Audio Finished Recording")

    # Convert the recorded audio to a numpy array
    audio = audio.flatten()
    audio = np.array(audio, dtype=np.float32)

    # Save the audio as a file
    filename = 'silence_calibration_audio.npy'
    np.save(filename, audio)
    print(f'Recorded audio saved to {filename}')

    return audio

def main():
    record_calibration_audio()

if __name__ == "__main__":
    main()