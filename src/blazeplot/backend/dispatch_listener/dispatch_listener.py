import sounddevice as sd
import numpy as np

class DispatchListener:
    def __init__(self, duration=10, fs=44100, silence_calibration_file="F:\\Programming\\projects\\radio\\BlazePlot\\src\\blazeplot\\backend\\dispatch_listener\\silence_calibration_audio.npy"):
        self.duration = duration
        self.fs = fs
        self.silence_calibration_file = silence_calibration_file
        self.speech_threshold = 0

    def calibrate_cutoff(self):
        # Load the audio file
        print("Loading Silence Calibration Audio")
        audio = np.load(self.silence_calibration_file)

        # Calculate the average audio level
        audio_level = np.mean(np.abs(audio))

        # Define a threshold for speech detection
        self.speech_threshold = 1.1 * audio_level

        print("Speech Threshold Set")

    def check_for_dispatch(self, audio_array):
        # Calculate the average audio level
        audio_level = np.mean(np.abs(audio_array))

        # Check if the audio level exceeds the global speech threshold
        if audio_level > self.speech_threshold:
            print("Speech detected")
            return True
        else:
            print("Silence detected")
            return False
