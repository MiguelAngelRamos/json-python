import json
from prettytable import PrettyTable

# CONSTANTE PARA MI JSON

ARCHIVO_PRODUCTOS = './data/productos.json'

def cargar_productos():
    try:
        with open(ARCHIVO_PRODUCTOS, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

def imprimir_productos():
    productos = cargar_productos()
    
    tabla = PrettyTable(["ID", "Nombre", "PRECIO", "STOCK" ])
    for producto in productos:
        tabla.add_row([producto['id'], producto['nombre'], producto['precio'], producto['stock'] ])
    print(tabla)

def menu():
    while True:
        print("1. Listar los productos desde el json")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == '1':
            imprimir_productos()
        elif opcion == '2':
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida! intenta de nuevo...")
            


if __name__ == '__main__':
    menu()