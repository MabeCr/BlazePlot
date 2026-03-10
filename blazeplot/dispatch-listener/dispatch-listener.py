import sounddevice as sd

duration = 5
fs = 44100

sd.default.samplerate = 44100
sd.default.channels = 2


def main():
    print("Recording Audio")
    myrecording = sd.rec(int(duration * fs))
    sd.wait()
    print("Audio Finished Recording")

    print("Playing Audio")
    sd.play(myrecording)
    sd.wait()
    print("Audio Finished Playing")

if __name__ == "__main__":
    main()