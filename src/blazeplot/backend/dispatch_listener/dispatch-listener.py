import sounddevice as sd
import numpy as np
import keyboard

duration = 10
fs = 44100

sd.default.samplerate = 44100

def calibrate_cutoff(silence_file):
    # Load the audio file
    print("Loading Silence Calibration Audio")
    audio = np.load(silence_file)

    # Calculate the average audio level
    audio_level = np.mean(np.abs(audio))

    # Define a threshold for speech detection
    speech_threshold = 1.1 * audio_level

    print(f"Speech Threshold: {speech_threshold}")
    return speech_threshold

def check_for_dispatch(audio_array, speech_threshold):
    # Calculate the average audio level
    audio_level = np.mean(np.abs(audio_array))

    # Check if the audio level exceeds the global speech threshold
    if audio_level > speech_threshold:
        print("Speech detected")
        return True
    else:
        print("Silence detected")
        return False

def main():
    print("Initializing Dispatch Listener")
    speech_threshold = calibrate_cutoff("./silence_calibration_audio.npy")

    print("Recording Audio")
    myrecording = sd.rec(int(duration * fs), channels=2, device="CABLE Output MME")
    sd.wait()
    print("Audio Finished Recording")

    print("Checking for Dispatch Audio")
    check_for_dispatch(myrecording, speech_threshold)

    print("Press Space Key to Continue")
    keyboard.wait('space')

    print("Playing Audio")
    sd.play(myrecording)
    sd.wait()
    print("Audio Finished Playing")

if __name__ == "__main__":
    main()