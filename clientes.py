#REGISTRAR NUEVO CLIENTE

class Cliente(object):
    def __init__(self, nombre, apellido, edad, dni, _id):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.dni=dni
        self._id=_id


    def registrar_cliente(self):

        while True:
            filename=input("Ingrese el NOMBRE de su archivo (o deje el campo vacío para retroceder): ")
            if filename=="":
                return None               
            filename+=".csv"
            
            try:
                file=open(filename, "rt")
                file=open(filename, "at")
                break
            except:
                print("No se encontró el archivo. Por favor, inténtelo de nuevo.\n")

        while True:
            nombre=input("Ingrese el nombre (o deje el campo VACÍO y presione ENTER para retroceder): ")
            if nombre=="":
                return None
            elif nombre.isalpha()==True:
                break
            print("El nombre solo puede contener LETRAS.\n")

        while nombre != "" and nombre.isalpha():

            while True:
                apellido=input("Ingrese el apellido: ")
                if apellido.isalpha()==True:
                    break
                print("El apellido solo puede contener LETRAS.\n")
            
            def ingresa_numero(numero):
                while True:
                    try:
                        valor=int(input(numero))
                        if valor>0:
                            return valor
                        print("El valor solo puede contener NÚMEROS NATURALES.\n")
                    except:
                        print("El valor solo puede contener NÚMEROS.\n")
            
            edad=ingresa_numero("Ingrese la edad: ")
            dni=ingresa_numero("Ingrese el DNI: ")
            _id=ingresa_numero("Ingrese el ID: ")

            vector=[nombre, apellido, edad, dni, _id]
            values=",".join(str(value) for value in (vector))+"\n"
            file.writelines([values])
            nombre=input("Ingrese OTRO nombre (si el campo está VACÍO o no contiene EXCLUSIVAMENTE letras al presionar ENTER, volverá al menú): ")
                
        file.close()

###########################################################################################

a=Cliente("","","","","")

def menu_clientes():
    while True:
        try:
            print("[1] AGREGAR cliente.\n")
            print("[0] Volver al menú principal.\n")
            opcion=int(input("Eliga una opción: "))
            if opcion==1:
                a.registrar_cliente()
            elif opcion==0:
                break
            else:
                print("Opción INVÁLIDA. Por favor, inténtelo de nuevo.\n")
        except:
            print("Opción INVÁLIDA. Por favor, inténtelo de nuevo.\n")

if __name__=="__main__":
    menu_clientes()
