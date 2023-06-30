import numpy as np
clientes = []
matriz = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
    ])

lotes = [
    {"numero": 1, "tamaño": "782m²", "precio": "$37,100,000"},
    {"numero": 2, "tamaño": "650 m²", "precio": "$32,500,000"},
    {"numero": 3, "tamaño": "1000 m²", "precio": "$55,000,000"},
    {"numero": 4, "tamaño": "280 m²", "precio": "$10,250,000"},
    {"numero": 5, "tamaño": "1200 m²", "precio": "$68,000,000"}
    ]


def mostrar_disponibilidad():
    print("LOTES DISPONIBLES:")
    for fila in matriz:
        for lote in fila:
            if lote == 0:
                print("[ ]", end=" ")
            else:
                print("[X]", end=" ")
        print()

def seleccionar_lote():
    fila = int(input("INGRESE FILA DEL LOTE: "))
    columna = int(input("INGRESE LA COLUMNA DEL LOTE: "))
    
    if matriz[fila-1][columna-1] == 0:
        rut = input("Ingrese su rut: ")
        nombre = input("Ingrese su nombre completo: ")
        telefono = input("Ingrese un numero de telefono: ")
        correo = input("Ingrese un correo: ")
        
        cliente = {
            "rut": rut,
            "nombre": nombre,
            "telefono": telefono,
            "correo": correo,
            "lote": (fila, columna)
        }
        
        clientes.append(cliente)
        matriz[fila-1][columna-1] = 1
        
        print("Has adquirido el lote correctamente.")
    else:
        print("El lote seleccionado no se encuentra disponible. Elija otro lote.")
        

def ver_detalles_lote():
    for cliente in clientes:
        lote = cliente["lote"]
        if matriz[lote[0]-1][lote[1]-1] == 1:
            for l in lotes:
                if l["numero"] == lote[1]:
                    print("Detalles del lote seleccionado:")
                    print(f"Número de lote: {l['numero']}")
                    print(f"Tamaño del terreno: {l['tamaño']}")
                    print(f"Precio: {l['precio']}")
                    break

def ver_clientes():
    print("Clientes que han comprado un lote:")
    for cliente in clientes:
        print(f"RUT: {cliente['rut']}")
        print(f"Nombre: {cliente['nombre']}")
        print(f"Teléfono: {cliente['telefono']}")
        print(f"Correo: {cliente['correo']}")
        lote = cliente["lote"]
        print(f"Lote seleccionado: ({lote[0]}, {lote[1]})")
        print()

def menu():
    while True:
        print("-------------LOTEOSDUOC-------------")
        print("--Este es el menú principal para adquirir terrenos--")
        print("")
        print("1. Ver disponibilidad de lotes ")
        print("2. Seleccionar un lote ")
        print("3. Ver detalle del lote seleccionado ")
        print("4. Ver Clientes ")
        print("5. Salir ")
        print()
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_disponibilidad()
        elif opcion == "2":
            seleccionar_lote()
        elif opcion == "3":
            ver_detalles_lote()
        elif opcion == "4":
            ver_clientes()
        elif opcion == "5":
            print("Gracias por visitar nuestra página")
            break
        else:
            print("Opción ingresada no válida. Seleccione nuevamente una opción.")


menu()