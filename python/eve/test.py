import whisper
import sounddevice as sd
from scipy.io.wavfile import write
from gtts import gTTS
import os
import string
from pydub import AudioSegment
from transformers import pipeline
import random
import time
from mutagen.mp3 import MP3


print('starting engine...')
classifier = pipeline("zero-shot-classification",
                      model="facebook/bart-large-mnli")

fs = 44100  # Sample rate
seconds = 5  # Duration of recording


def speak(ans):
    myobj = gTTS(text=ans, lang='en', slow=False)
    myobj.save("speech.mp3")    
    audio = MP3("speech.mp3")
    leng = audio.info.length
    os.system("speech.mp3")
    time.sleep(leng)


def information(text):
    answer = ''
    return answer


def meaningof(text):
    answer =''
    return answer
#returns a summarized meaning for something

def greetings(text):
    answer = ''
    if 'hi' in text:
        answer = random.choice(['hi boss', 'hi fernando', 'hi master'])
    if 'hello' in text:
        answer = random.choice(['hello boss', 'hello fernando', 'hello master'])
    return answer

def question(text):
    answer = ''
    if 'what is your purpose' in text:
        answer = 'I was designed by fernando martins and my purpose is to take over the world'
    if 'who is your creator' in text or 'who created you' in text:
        answer = 'I was designed by fernando'
    if 'who are you' in text:
        answer = 'I am an artificial intelligence designed by fernando martins, my name is NOVA'
    if 'who is fernando' in text:
        answer = 'he is my creator'
    return answer

while True:
    ans = ''
    print("listening")

# VOICE RECORD PROCCESS
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file 

# CHECK IF THERE IS VOICE
    audio_segment = AudioSegment.from_file("output.wav")
    intensity = int(audio_segment.dBFS)
    if intensity < -62:
        print("no voice")
        continue

# SPEECH TO TEXT PROCCESS
    model = whisper.load_model("tiny")
    result = model.transcribe("output.wav", language= 'en', fp16=False) 
    q = result['text'].lower().strip().translate(str.maketrans('', '', string.punctuation))
    if q == 'you' or q == '':
        continue
    print(q)

# CALLING EVE
    if q == 'evening':
        speak(random.choice(['yes']))

#FUNCTION GOES HERE
    sequence_to_classify = q
    candidate_labels = ['greetings', 'task', 'question']
    cont = classifier(sequence_to_classify, candidate_labels)
    context = cont['labels'][0]

    if context == 'greetings':
        ans = greetings(q)
    if context == 'question':
        if 'meaning' in q:
            ans = meaningof(q)
        if 'what information' in q:
            ans = information(q)
        else:
            ans = question(q)

    if context == 'task':
        pass
    

#SPEAKS
    if ans != '':
        speak(ans)