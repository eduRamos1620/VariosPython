#Librerias necesarias
#pip install SpeechRecognition / libreria para reconocimiento de voz
#pip install pyttsx3 /Convierte texto a voz

import speech_recognition as sr
import webbrowser
import pyttsx3

#Llamamos a Recognizer
reconocer = sr.Recognizer()

#Iniciamos nuestro asistente
asistente = pyttsx3.init()

def hablar():
    mic = sr.Microphone()
    with mic as source:
        audio = reconocer.listen(source)
    
    text = reconocer.recognize_google(audio, language="ES")
    
    return text.lower()

if 'obito' in hablar():
    asistente.say("Que quieres buscar")
    asistente.runAndWait()
    text = hablar()
    webbrowser.open(f'https://listado.mercadolibre.com.mx/{text}')