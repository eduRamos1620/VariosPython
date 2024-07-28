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

#se crea funcion hablar
def hablar():
    #Iniciamos el microfono
    mic = sr.Microphone()
    
    #micrfono escuchando
    with mic as source:
        #audio guarda lo que microfono escucha
        audio = reconocer.listen(source)
    
    #guardamos en una variable lo que escucho 
    text = reconocer.recognize_google(audio, language='ES')
    
    #retornamos el texto guardado
    return text.lower()

#si Max existe dentro de la funcion
if 'max' in hablar():
    #computadora nos responde
    asistente.say("Que quieres buscar")
    #espera a que digamos algo
    asistente.runAndWait()
    #llama la funcion hablar y guarda lo que queremos comprar
    text = hablar()
    #realiza la buqueda en el url indicado sobre lo que buscamos
    webbrowser.open(f'https://listado.mercadolibre.com.mx/{text}')
else:
    print ("no has dicho nada")