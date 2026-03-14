import whisper
import numpy as np
import sounddevice as sd
import keyboard
import soundfile as sf

from blazeplot.backend.dispatch_listener import DispatchListener

model = whisper.load_model("tiny")
listener = DispatchListener()

duration = 20
fs = 16000

def transcribe_audio(audio):
    result = model.transcribe(np.squeeze(audio))
    return result

def main():
    print("Initializing Dispatch Listener")
    try:
        print("Silence calibration file found! Setting speech threshold...")
        listener.calibrate_cutoff()
    except FileNotFoundError:
        print("No silence_calibration_audio.npy file found. Please provide a silence calibration file before trying again. Exiting...")
        return

    print("Recording Audio")
    myrecording = sd.rec(int(duration * fs), samplerate=fs,channels=1, device="CABLE Output MME", dtype=np.float32)
    sd.wait()
    print("Audio Finished Recording")

    print("Checking for Dispatch Audio")
    listener.check_for_dispatch(myrecording)

    print("Press Space Key to Continue")
    keyboard.wait('space')

    print("Playing Audio")
    sd.play(myrecording, samplerate=fs)
    sd.wait()
    print("Audio Finished Playing")

    print("Transcribing Audio")
    transcribed_audio = transcribe_audio(myrecording)
    print(transcribed_audio["text"])

if __name__ == "__main__":
    main()