from gtts import gTTS
import os

mytext = " Aspiring Developer on Full Stack web development Using Python Django and really curious about tech and programming My Skills are Python, Django, HTML, CSS, JavaScript, jQuery and Bootstrap" and looking forward to meet you
language = "en"
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("result.mp3")
os.system("result.mp3")
