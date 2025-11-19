#MENÚ PRINCIPAL INTERACTIVO

def menu_principal():
    while True:
        try:
            print("------MENÚ PRINCIPAL------\n")
            print("[1] Registrar nuevo cliente\n")
            print("[2] Solicitar turno\n")
            print("[3] Listar turnos existentes\n")
            print("[4] Modificar o cancelar turno\n")
            print("[5] Guardar datos en CSV / Cargar desde Dict\n")
            print("[0] Salir\n")

            opcion=int(input("Elija una opción: "))

            if opcion==1:
                print("1")
            elif opcion==2:
                print("2")
            elif opcion==3:
                print("3")
            elif opcion==4:
                print("4")
            elif opcion==5:
                print("5")
            elif opcion==0:
                break
            else:
                print("Opción INVÁLIDA. Por favor, inténtelo de nuevo.\n")
            
        except:
            print("Opción INVÁLIDA. Por favor, inténtelo de nuevo.\n")

menu_principal()
