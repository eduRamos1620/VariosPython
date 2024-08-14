import os

shutdown = input("Quieres apagar el equipo? si/no: ").lower()

if shutdown == 'si':
    os.system('shutdown /s /t 10')#10 segundos para que apague
else:
    exit()