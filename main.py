import os
import DAO.CRUDCliente
from DTO.Cliente import Cliente

# TIPOS DE CLIENTES
TIPOS = {
    1: "Cliente Normal",
    2: "VIP",
    3: "Empresa"
}

# MENÚ PRINCIPAL
def menuPrincipal():
    os.system('cls')
    print("======================")
    print("    MENÚ PRINCIPAL    ")
    print("======================")
    print("1. INGRESAR CLIENTE")
    print("2. MOSTRAR CLIENTES")
    print("3. MODIFICAR CLIENTE")
    print("4. ELIMINAR CLIENTE")
    print("5. SALIR")
    print("======================")

# INGRESAR CLIENTE Y SUS DATOS
def ingresarDatos():
    os.system('cls')
    print("======================")
    print("   INGRESAR CLIENTE   ")
    print("======================")

    run = input("RUN: ")
    nombre = input("NOMBRE: ")
    apellido = input("APELLIDO: ")
    direccion = input("DIRECCIÓN: ")
    fono = input("TELÉFONO: ")
    correo = input("CORREO: ")

    datos = DAO.CRUDCliente.mostrarTipos()

    print("=====================")
    for d in datos:
        print(f"{d[0]} - {d[1]}")
    print("=====================")

    # VALIDACIÓN FUERTE (IMPORTANTE)
    tipo = 0
    while tipo not in TIPOS:
        try:
            tipo = int(input("TIPO CLIENTE (1-3): "))
        except:
            tipo = 0

    monto = int(input("MONTO CRÉDITO: "))
    cliente = Cliente(run, nombre, apellido, direccion, fono, correo, monto, 0, tipo)
    ok = DAO.CRUDCliente.agregar(cliente)

    print("\nCLIENTE INGRESADO CORRECTAMENTE" if ok else "\nERROR AL INGRESAR CLIENTE")
    input("\nPRESIONE UNA TECLA PARA CONTINUAR...")

# MOSTRAR LA LISTA DE CLIENTES
def mostrarTodo():
    os.system('cls')
    print("=" * 140)
    print("   LISTA DE CLIENTES   ")
    print("=" * 140)

    print("{:<3} {:<12} {:<10} {:<10} {:<15} {:<10} {:<20} {:<10} {:<8} {:<20}".format(
        "ID", "RUN", "NOMBRE", "APELLIDO", "DIRECCION", "FONO", "CORREO", "CREDITO", "DEUDA", "TIPO"
    ))

    print("=" * 140)

    datos = DAO.CRUDCliente.mostrarTodos()

    TIPOS = {
        "Cliente Normal": "1 - Cliente Normal",
        "VIP": "2 - VIP",
        "Empresa": "3 - Empresa"
    }

    for d in datos:
        tipo_nombre = TIPOS.get(d[9], f"0 - {d[9]}")
        print("{:<3} {:<12} {:<10} {:<10} {:<15} {:<10} {:<20} {:<10} {:<8} {:<20}".format(
            d[0], d[1], d[2], d[3], d[4], d[5], d[6], d[7], d[8], tipo_nombre
        ))

    input("\nPRESIONE UNA TECLA PARA CONTINUAR...")

# MODIFICAR DATOS DE UN CLIENTE
def modificarCliente():
    os.system('cls')
    mostrarTodo()

    idc = int(input("\nID A MODIFICAR: "))
    datos = DAO.CRUDCliente.consultaParticular(idc)

    if not datos:
        print("CLIENTE NO ENCONTRADO")
        input("PRESIONE UNA TECLA PARA CONTINUAR...")
        return

    tipo = 0
    while tipo not in TIPOS:
        try:
            tipo = int(input(f"Tipo [{datos[9]}]: "))
        except:
            tipo = datos[9]

    cliente = Cliente(
        datos[1],
        input(f"Nombre [{datos[2]}]: ") or datos[2],
        input(f"Apellido [{datos[3]}]: ") or datos[3],
        input(f"Dirección [{datos[4]}]: ") or datos[4],
        input(f"Teléfono [{datos[5]}]: ") or datos[5],
        input(f"Correo [{datos[6]}]: ") or datos[6],
        int(input(f"Monto Crédito [{datos[7]}]: ") or datos[7]),
        int(input(f"Deuda [{datos[8]}]: ") or datos[8]),
        tipo
    )

    cliente.id = datos[0]
    DAO.CRUDCliente.editar(cliente)

    print("\nCLIENTE MODIFICADO CORRECTAMENTE")
    input("\nPRESIONE UNA TECLA PARA CONTINUAR...")

# ELIMINAR CLIENTE
def eliminarCliente():
    os.system('cls')
    mostrarTodo()

    idc = int(input("\nID DE CLIENTE A ELIMINAR: "))
    DAO.CRUDCliente.eliminar(idc)

    print("\nCLIENTE ELIMINADO CORRECTAMENTE" if idc else "\nERROR AL ELIMINAR CLIENTE")
    input("\nPRESIONE UNA TECLA PARA CONTINUAR...")

# MENÚ
while True:
    menuPrincipal()
    opcion = int(input("SELECCIONE UNA OPCIÓN: "))

    if opcion == 1:
        ingresarDatos()
    elif opcion == 2:
        mostrarTodo()
    elif opcion == 3:
        modificarCliente()
    elif opcion == 4:
        eliminarCliente()
    elif opcion == 5:
        break
    else:
        print("OPCIÓN INVÁLIDA")
        input("PRESIONE UNA TECLA PARA VOLVER A INTENTARLO...")
