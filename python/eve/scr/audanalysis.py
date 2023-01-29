from pydub import AudioSegment
audio_segment = AudioSegment.from_file("output.wav")
print(f"Intensity: {audio_segment.dBFS}")
inten = int(audio_segment.dBFS)
if inten < -62:
    print("no voice")
else:
    print("voice")
    