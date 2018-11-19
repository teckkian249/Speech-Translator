from gtts import gTTS
from playsound import playsound
tts = gTTS(text='Good morning', lang='en')
tts.save("./recordings/good.mp3")

playsound("./recordings/good.mp3")