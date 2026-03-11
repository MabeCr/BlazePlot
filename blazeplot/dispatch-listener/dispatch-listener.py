import sounddevice as sd
import keyboard

duration = 10
fs = 44100

sd.default.samplerate = 44100


def main():
    print("Recording Audio")
    myrecording = sd.rec(int(duration * fs), channels=2, device="CABLE Output MME")
    sd.wait()
    print("Audio Finished Recording")

    print("Press Space Key to Continue")
    keyboard.wait('space')

    print("Playing Audio")
    sd.play(myrecording)
    sd.wait()
    print("Audio Finished Playing")

if __name__ == "__main__":
    main()