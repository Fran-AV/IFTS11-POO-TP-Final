import datetime
from sincronizador import sincronizar

class Turnos(object):
    def __init__(self, id_cl, date, time):
        self.id_cl=id_cl
        self.date=date
        self.time=time

########################################################################################    

    def crear_nuevo(self):
        filename=input("Nombre su archivo (o deje el campo VACÍO y presione ENTER para retroceder): ")
        if filename=="":
            return None
        filename+=".csv"
        file=open(filename, "w")
        keys=["id_cl", "date", "time"]
        line_csv=",".join(keys)+"\n"
        file.writelines([line_csv])
        id_cl=input("Ingrese el ID de cliente (o deje el campo VACÍO y presione ENTER para retroceder): ")
        
        while id_cl != "":
            
            while True:
                try:
                    id_cl_int = int(id_cl)
                    if id_cl_int>0:
                        break
                    print("El ID solo puede contener NÚMEROS NATURALES.\n")
                except:
                    print("El ID solo puede contener NÚMEROS.\n")
                    a.crear_nuevo()

    
            def ingr_date():
                while True:
                    try:
                        dia=int(input("Ingrese el DÍA: "))
                        mes=11
                        anio=2025
                        date=datetime.date(anio, mes, dia)
                        if dia>2 and dia<8:
                            return date
                        print("Fecha inválida. Por favor, inténtelo de nuevo.\n")
                    except:
                        print("Fecha inválida. Por favor, inténtelo de nuevo.\n")

            def ingr_time():
                while True:
                    try:
                        hora=int(input("Ingrese la HORA: "))
                        minuto=int(input("Ingrese el MINUTO: "))
                        time=datetime.time(hora, minuto)
                        if hora>10 and hora<15:
                            if minuto==0 or minuto==30:
                                return time
                        print("Fecha inválida. Por favor, inténtelo de nuevo.\n")
                    except:
                        print("Hora inválida. Por favor, inténtelo de nuevo.\n")

            _date=ingr_date()
            _time=ingr_time()
            str_date =_date.strftime("%d-%m")
            str_time =_time.strftime("%H:%M")
            
            vector=[id_cl, str_date, str_time]
            values=",".join(str(value) for value in (vector)) + "\n"
            file.writelines([values])
            id_cl=input("Ingrese OTRO ID de cliente (o deje el campo VACÍO para finalizar): ")
            
        file.close()
        sincronizar("espacios_libres.csv", filename)

#########################################################################################

    def agregar_turno(self):
        
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
        
        id_cl=input("Ingrese el ID de cliente (o deje el campo VACÍO y presione ENTER para retroceder): ")
        
        while id_cl != "":
            
            while True:
                try:
                    id_cl_int = int(id_cl)
                    if id_cl_int>0:
                        break
                    print("El ID solo puede contener NÚMEROS NATURALES.\n")
                except:
                    print("El ID solo puede contener NÚMEROS.\n")
                    a.agregar_turno()

    
            def ingr_date():
                while True:
                    try:
                        dia=int(input("Ingrese el DÍA: "))
                        mes=11
                        anio=2025
                        date=datetime.date(anio, mes, dia)
                        if dia>2 and dia<8:
                            return date
                        print("Fecha inválida. Por favor, inténtelo de nuevo.\n")
                    except:
                        print("Fecha inválida. Por favor, inténtelo de nuevo.\n")

            def ingr_time():
                while True:
                    try:
                        hora=int(input("Ingrese la HORA: "))
                        minuto=int(input("Ingrese el MINUTO: "))
                        time=datetime.time(hora, minuto)
                        if hora>10 and hora<15:
                            if minuto==0 or minuto==30:
                                return time
                        print("Fecha inválida. Por favor, inténtelo de nuevo.\n")
                    except:
                        print("Hora inválida. Por favor, inténtelo de nuevo.\n")

            _date=ingr_date()
            _time=ingr_time()
            str_date= _date.strftime("%d-%m")
            str_time= _time.strftime("%H:%M")
            
            vector=[id_cl, str_date, str_time]
            values=",".join(str(value) for value in (vector)) + "\n"
            
            """
            gf=DB(filename)
            k=gf.read()
            turnos=set()
        
            for diccionario in k:
                str(diccionario)
                turnos.add(diccionario)
                
            if values not in turnos:
                file.writelines([values])
                turnos.add(values)
            else:
                print("Este horario ya está ocupado.")
            """ 
            
            file.writelines([values])
            id_cl=input("Ingrese OTRO ID de cliente (o deje el campo para finalizar): ")
            
        file.close()
        sincronizar("espacios_libres.csv", filename)

#######################################################################################

a=Turnos("","","")

#######################################################################################

def menu_turnos():
    while True:
        try:
            print("[1] CREAR un registro de turnos NUEVO.\n")
            print("[2] AGREGAR turno a un registro EXISTENTE.\n")
            print("[0] Volver al menú principal.\n")
            opcion=int(input("Eliga una opción: "))
            if opcion==1:
                a.crear_nuevo()
            elif opcion==2:
                a.agregar_turno()
            elif opcion==0:
                break
            else:
                print("Opción INVÁLIDA. Por favor, inténtelo de nuevo.\n")
        except:
            print("Opción INVÁLIDA. Por favor, inténtelo de nuevo.\n")

if __name__=="__main__":
    menu_turnos()
