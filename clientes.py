#REGISTRAR NUEVO CLIENTE

class Cliente(object):
    def __init__(self, nombre, apellido, edad, dni, id):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.dni=dni
        self.id=id
        
    def crear_registro_nuevo(self):
        filename=input("Nombre su archivo: ")
        filename+=".csv"
        file=open(filename, "wt")                        #WRITE TEXT
        keys=["nombre", "apellido", "edad", "dni", "id"]
        line_csv=",".join(keys)+"\n"
        file.writelines([line_csv])

        while True:
            nombre=input("Ingrese el nombre (o deje el campo VACÍO y presione ENTER para retroceder): ")
            if nombre=="":
                crear_o_agregar()
            elif nombre.isalpha()==True:
                break
            print("El nombre solo puede contener LETRAS.\n")

        while nombre != "" and nombre.isalpha():

            while True:
                apellido=input("Ingrese el apellido: ")
                if apellido.isalpha()==True:
                    break
                print("El apellido solo puede contener LETRAS.\n")
            while True:
                try:
                    edad=int(input("Ingrese la edad: "))
                    if edad>0:
                        break
                    print("La edad solo puede contener NÚMEROS NATURALES.\n")
                except:
                    print("La edad solo puede contener NÚMEROS.\n")
            while True:
                try:
                    dni=int(input("Ingrese el DNI: "))
                    if dni>0:
                        break
                    print("El DNI solo puede contener NÚMEROS NATURALES.\n")
                except:
                    print("El DNI solo puede contener NÚMEROS.\n")

            while True:
                try:
                    id=int(input("Ingrese el ID: "))
                    if id>0:
                        break
                    print("El ID solo puede contener NÚMEROS NATURALES.\n")
                except:
                    print("El ID solo puede contener NÚMEROS.\n")

            vector=[nombre, apellido, edad, dni, id]
            values=",".join(str(value) for value in (vector)) + "\n"
            file.writelines([values])
            nombre=input("Ingrese OTRO nombre (si el campo está VACÍO o no contiene EXCLUSIVAMENTE letras al presionar ENTER, volverá al menú): ")
                
        file.close()



    def registrar_cliente(self):

        while True:
            filename=input("Ingrese el NOMBRE de su archivo: ")
            if filename=="":
                crear_o_agregar()
                
            filename+=".csv"
            try:
                file=open(filename, "rt")
                file=open(filename, "at")                #APPEND TEXT
                break
            except:
                print("El archivo no fue encontrado.\n")

        while True:
            nombre=input("Ingrese el nombre (o deje el campo VACÍO y presione ENTER para retroceder): ")
            if nombre=="":
                crear_o_agregar()
                
            elif nombre.isalpha()==True:
                break
            print("El nombre solo puede contener LETRAS.\n")

        while nombre != "" and nombre.isalpha():

            while True:
                apellido=input("Ingrese el apellido: ")
                if apellido.isalpha()==True:
                    break
                print("El apellido solo puede contener LETRAS.\n")
            while True:
                try:
                    edad=int(input("Ingrese la edad: "))
                    if edad>0:
                        break
                    print("La edad solo puede contener NÚMEROS NATURALES.\n")
                except:
                    print("La edad solo puede contener NÚMEROS.\n")
            while True:
                try:
                    dni=int(input("Ingrese el DNI: "))
                    if dni>0:
                        break
                    print("El DNI solo puede contener NÚMEROS NATURALES.\n")
                except:
                    print("El DNI solo puede contener NÚMEROS.\n")

            while True:
                try:
                    id=int(input("Ingrese el ID: "))
                    if id>0:
                        break
                    print("El ID solo puede contener NÚMEROS NATURALES.\n")
                except:
                    print("El ID solo puede contener NÚMEROS.\n")

            vector=[nombre, apellido, edad, dni, id]
            values=",".join(str(value) for value in (vector)) + "\n"
            file.writelines([values])
            nombre=input("Ingrese OTRO nombre (si el campo está VACÍO o no contiene EXCLUSIVAMENTE letras al presionar ENTER, volverá al menú): ")
                
        file.close()


a=Cliente("","","","","")


def crear_o_agregar():
    while True:
        try:
            print("¿Quiere crear un registro NUEVO o agregar un cliente a un registro EXISTENTE?\n")
            print("[1] CREAR registro nuevo (se BORRARÁ el registro EXISTENTE).\n")
            print("[2] AGREGAR cliente a un registro existente.\n")
            print("[0] Volver al menú principal.\n")

            opcion=int(input("Eliga una opción: "))

            if opcion==1:
                a.crear_registro_nuevo()
            elif opcion==2:
                a.registrar_cliente()
            elif opcion==0:
                break
                
            else:
                print("Opción INVÁLIDA. Por favor, inténtelo de nuevo.\n")
        
        except:
            print("Opción INVÁLIDA. Por favor, inténtelo de nuevo.\n")

crear_o_agregar()
