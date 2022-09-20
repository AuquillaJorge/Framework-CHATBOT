import requests
import speech_recognition as sr     
import subprocess
#from subprocess import call
from gtts import gTTS


# sender = input("What is your name?\n")
bot_message = ""
message=""
r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})
print("Bot dice, ",end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

myobj = gTTS(text=bot_message, lang='es-us')
myobj.save("welcome.mp3")
print('Recibido')
# Playing the converted file


#subprocess.call(['start', "welcome.mp3", '--play-and-exit'],shell=True)
#subprocess.call(['cvlc', "welcome.mp3", '--play-and-exit'])
#subprocess.run(['vlc', r'welcome.mp3','--play-and-exit', '--rate=1.5'])
#playsound('welcome.mp3')
#call(["start", "welcome.wav"],shell=True)

while bot_message != "Adios" or bot_message!='Gracias':

    r = sr.Recognizer()  # inicializar el reconocedor
    with sr.Microphone() as source:  # menciona la fuente será el micrófono o los archivos de audio.
        print("Hablar de cualquier cosa :")
        audio = r.listen(source)  # escuchar la fuente
        try:
            message = r.recognize_google(audio,language='es-EC')  # utilizar el reconocedor para convertir nuestra parte de audio en texto.
            print("Usted dijo : {}".format(message))

        except:
            print("Lo siento, no pude reconocer su voz")   # En caso de que la voz no se reconozca claramente
    if len(message)==0:
        continue
    print("Enviando mensaje ahora...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot dice, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message,lang='es-us')
    myobj.save("welcome.mp3")
    print('Recibido')
    # Reproducir el archivo convertido
    # subprocess.call(['vlc', "welcome.mp3", '--play-and-exit'])
    #subprocess.Popen(r'welcome.mp3',shell = True)
    #playsound('welcome.mp3')

    #subprocess.call(['start', "welcome.mp3", '--play-and-exit'],shell=True)
    #subprocess.call(['cvlc', "welcome.mp3", '--play-and-exit'])
    #call(["start", "welcome.wav"],shell=True)

    if bot_message.lower()=='Adios':
        break









