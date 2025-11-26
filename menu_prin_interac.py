#MENÚ PRINCIPAL INTERACTIVO

from clientes import menu_clientes
from turnos import menu_turnos
from listar_turnos import listar_turnos
from modificador_turnos import menu_cambio

def menu_principal():
    while True:
        try:
            print("------MENÚ PRINCIPAL------\n")
            print("[1] Registrar nuevo cliente\n")
            print("[2] Solicitar turno\n")
            print("[3] Listar turnos existentes\n")
            print("[4] Modificar o cancelar turno\n")
            print("[0] Salir\n")

            opcion=int(input("Elija una opción: "))

            if opcion==1:
                menu_clientes()
            elif opcion==2:
                menu_turnos()
            elif opcion==3:
                listar_turnos()
            elif opcion==4:
                menu_cambio()
            elif opcion==0:
                break
            else:
                print("Opción INVÁLIDA. Por favor, inténtelo de nuevo.\n")
            
        except:
            print("Opción INVÁLIDA. Por favor, inténtelo de nuevo.\n")

menu_principal()
