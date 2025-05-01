# run.py
import sys
import menu

if __name__ == "__main__":
    menu.iniciar()

# config.py
import sys

DATABASE_PATH = 'clientes.csv'
if 'pytest' in sys.argv[0]:
    DATABASE_PATH = 'tests/clientes_test.csv'
