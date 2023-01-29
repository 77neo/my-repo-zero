from mutagen.mp3 import MP3
audio = MP3("speech.mp3")
print(audio.info.length)
