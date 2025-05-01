import csv
from Cliente import Cliente

try:
    import config
except ImportError:
    raise ImportError("El módulo 'config' no se encuentra. Asegúrate de que el archivo 'config.py' existe y está en el mismo directorio o en el PYTHONPATH.")
class Clientes:
    lista = []

    try:
        with open(config.DATABASE_PATH, newline="\n") as fichero:
            reader = csv.reader(fichero, delimiter=";")
            for dni, nombre, apellido in reader:
                cliente = Cliente(dni, nombre, apellido)
                lista.append(cliente)
    except FileNotFoundError:
        # Handle the case where the database file does not exist
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
            pass  # Create an empty file

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, "w", newline="\n") as fichero:
            writer = csv.writer(fichero, delimiter=";")
            for c in Clientes.lista:
                writer.writerow((c.dni, c.nombre, c.apellido))

    @staticmethod
    def buscar(dni: str):
        return next((c for c in Clientes.lista if c.dni == dni), None)

    @staticmethod
    def crear(dni: str, nombre: str, apellido: str):
        cliente = Cliente(dni, nombre, apellido)
        Clientes.lista.append(cliente)
        Clientes.guardar()
        return cliente

    @staticmethod
    def modificar(dni: str, nombre: str, apellido: str):
        cliente = Clientes.buscar(dni)
        if cliente:
            cliente.nombre = nombre
            cliente.apellido = apellido
            Clientes.guardar()
            return cliente

    @staticmethod
    def borrar(dni: str):
        cliente = Clientes.buscar(dni)
        if cliente:
            Clientes.lista.remove(cliente)
            Clientes.guardar()
            return cliente

