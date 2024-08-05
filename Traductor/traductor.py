#pip install translate

from translate import Translator

#Definimos los lenguajes
translator = Translator(from_lang='spanish', to_lang='english')

#Solicitamos la frase o palabra
frase = input('Ingresa la frase o palabra a traducir: ')

#Guardamos la frase ya traducida
frase_traducida = translator.translate(frase)

#Imprimimos
print(f'Tu frase o palabra traducida es: {frase_traducida}')