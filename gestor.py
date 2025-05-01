# Estructura del proyecto en POO y TDA





# gestor/helpers.py
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

# gestor/menu.py
import database as db
import helpers

def iniciar():
    while True:
        helpers.limpiar_pantalla()
        print("========================")
        print("  BIENVENIDO AL Manager ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Buscar cliente      ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Cerrar el Manager   ")
        print("========================")
        opcion = input("> ")

        helpers.limpiar_pantalla()
        if opcion == '1':
            for cliente in db.Clientes.lista:
                print(cliente)

        elif opcion == '2':
            dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente if cliente else "Cliente no encontrado.")

        elif opcion == '3':
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 chars)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")

        elif opcion == '4':
            dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Nombre [{cliente.nombre}]").capitalize()
                apellido = helpers.leer_texto(2, 30, f"Apellido [{cliente.apellido}]").capitalize()
                db.Clientes.modificar(dni, nombre, apellido)
                print("Cliente modificado correctamente.")
            else:
                print("Cliente no encontrado.")

        elif opcion == '5':
            dni = helpers.leer_texto(3, 3, "DNI (2 ints y 1 char)").upper()
            if db.Clientes.borrar(dni):
                print("Cliente borrado correctamente.")
            else:
                print("Cliente no encontrado.")

        elif opcion == '6':
            print("Saliendo...")
            break

        input("\nPresiona ENTER para continuar...")


