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
    print(productos)
    tabla = PrettyTable(["ID", "Nombre", "PRECIO", "STOCK" ])
    for producto in productos:
        tabla.add_row([producto['id'], producto['nombre'], producto['precio'], producto['stock'] ])
    print(tabla)
    
def guardar_producto(productos):
    try:
        with open(ARCHIVO_PRODUCTOS, 'w') as archivo:
            return json.dump(productos, archivo, indent=4)
    except ValueError as error:
        print(f"Error al abrir el archivo: {error}")

def actualizar_producto():
    id_producto = int(input("ID del producto a actualizar: "))
    productos = cargar_productos()
    
    for producto in productos:
        if producto['id'] == id_producto:
            producto['nombre'] = input("Nuevo nombre para el producto: ")
            producto['precio'] = float(input("Nuevo precio para el producto: "))
            producto['stock'] = int(input("Nuevo stock para el producto: "))
            
            guardar_producto(productos)
            print("Producto actualizado exitosamente")
            return
    print("Producto no encontrado")
     
    

def agregar_producto():
    # Solicito informacion al cliente
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    stock = int(input("Stock del producto: "))
    
    # Cargar los productos existentes
    productos = cargar_productos()
    
    # Vamos a generar un ID para cada producto 
    id_nuevo = max([producto['id'] for producto in productos], default=0) + 1
    
    productos.append({
        'id': id_nuevo,
        'nombre': nombre,
        'precio': precio,
        'stock': stock
    })
    
    guardar_producto(productos)
    print("Productos agregado exitosamente.")


def menu():
    while True:
        print("1. Listar los productos desde el json")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == '1':
            imprimir_productos()
        elif opcion == '2':
            agregar_producto()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opcion no valida! intenta de nuevo...")
            


if __name__ == '__main__':
    menu()