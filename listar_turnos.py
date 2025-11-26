from transformador import DB

def listar_turnos():
    
    while True:
        filename=input("Ingrese el nombre de su registro de TURNOS: ")
        filename+=".csv"
        try:
            open(filename, "rt")
            break
        except:
            print("No se encontró el archivo. Por favor, inténtelo de nuevo.\n")
        
    db=DB(filename)
    p=db.read()
    i=0
    while i<len(p):
        x=p[i]
        b=x.items()
        for key, value in b:
            print(f"{key}: {value}")
        i+=1

if __name__=="__main__":
    listar_turnos()
