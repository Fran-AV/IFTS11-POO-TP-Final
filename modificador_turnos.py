from transformador import DB
from transformador import dict2csv
import datetime

def modificar_turno(id_cl):

    while True:
        try:
            valor=int(input(id_cl))
            if valor>0:
                break
            print("El ID solo puede contener NÚMEROS NATURALES.\n")
        except:
            print("El ID solo puede contener NÚMEROS.\n")

    while True:
            filename=input("Ingrese el NOMBRE de su registro de TURNOS (o deje el campo vacío para retroceder): ")
            if filename=="":
                return None               
            filename+=".csv"
            
            try:
                file=open(filename, "rt")
                break
            except:
                print("No se encontró el archivo. Por favor, inténtelo de nuevo.\n")
    
    db=DB(filename)
    b=db.read()
    keys=list(b[0].keys())
    i=0
    while i<len(b):
        c=b[i][keys[0]]
        
        if c==str(valor):
            
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

            date_nuevo=ingr_date()
            time_nuevo=ingr_time()
            str_date_nuevo = date_nuevo.strftime("%d-%m")
            str_time_nuevo = time_nuevo.strftime("%H:%M")
            
            turno_borrado=b[i]
            date=turno_borrado[keys[1]]
            time=turno_borrado[keys[2]]

            b.pop(i)
            m={"id_cl": valor, "date": str_date_nuevo, "time": str_time_nuevo}
            b.append(m)

            th=DB("espacios_libres.csv")
            y=th.read()
            k=0
            while k<len(y):
                slot_date=y[k]["date"].strip()
                slot_time=y[k]["time"].strip()
                if slot_date==str_date_nuevo and slot_time==str_time_nuevo:
                    y.pop(k)
                    break
                k+=1

            n={"date":date, "time":time}
            y.append(n)
            break
        i+=1
    
    return dict2csv(b), dict2csv(y)

###########################################################################################

def borrar_turno(id_cl):
    
    while True:
        try:
            valor=int(input(id_cl))
            if valor>0:
                break
            print("El ID solo puede contener NÚMEROS NATURALES.\n")
        except:
            print("El ID solo puede contener NÚMEROS.\n")

    while True:
        filename=input("Ingrese el NOMBRE de su registro de TURNOS (o deje el campo vacío para retroceder): ")
        if filename=="":
            return None               
        filename+=".csv"
        
        try:
            file=open(filename, "rt")
            break
        except:
            print("No se encontró el archivo. Por favor, inténtelo de nuevo.\n")

    db=DB(filename)
    b=db.read()
    keys=list(b[0].keys())
    i=0
    while i<len(b):
        c=b[i][keys[0]]
        if c==str(valor):
            turno_borrado=b[i]
            date=turno_borrado[keys[1]]
            time=turno_borrado[keys[2]]
            b.pop(i)
        i+=1
    
    th=DB("espacios_libres.csv")
    y=th.read()
    m={"date":date, "time":time}
    y.append(m)
    
    return dict2csv(b), dict2csv(y)

###########################################################################################

def menu_cambio():
    while True:
        try:
            print("[1] MODIFICAR turno.\n")
            print("[2] ELIMINAR turno.\n")
            print("[0] Volver al menú principal.\n")

            opcion=int(input("Eliga una opción: "))

            if opcion==1:
                modificar_turno("Ingrese el ID de cliente cuyo turno se quiere MODIFICAR: ")
            elif opcion==2:
                borrar_turno("Ingrese el ID de cliente cuyo turno se quiere ELIMINAR: ")
            elif opcion==0:
                break
            else:
                print("Opción INVÁLIDA. Por favor, inténtelo de nuevo.\n")
        except:
            print("Opción INVÁLIDA. Por favor, inténtelo de nuevo.\n")

if __name__=="__main__":
    menu_cambio()
