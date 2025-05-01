import os
import platform
import re

def limpiar_pantalla():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    if mensaje:
        print(mensaje)
    while True:
        texto = input("> ")
        if longitud_min <= len(texto) <= longitud_max:
            return texto

def dni_valido(dni, lista):
    if not re.match(r'[0-9]{2}[A-Z]$', dni):
        print("DNI incorrecto, debe cumplir el formato.")
        return False
    if any(cliente.dni == dni for cliente in lista):
        print("DNI utilizado por otro cliente.")
        return False
    return True