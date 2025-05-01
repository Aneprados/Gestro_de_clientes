import sys
from Lanzador import Lanzador

# Configuración de la base de datos
DATABASE_PATH = 'clientes.csv'
if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'tests/clientes_test.csv'

if __name__ == "__main__":
    Lanzador.iniciar()