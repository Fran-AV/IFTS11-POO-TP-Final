
class Transformador(object):

    def __init__(self, attrb, tipo_registro=None):
        self.keys=attrb
        self.tipo_registro = tipo_registro or Registro    #Por defecto, usa Registro genérico.
    

    def todict(self, values):
        if len(values) != len(self.keys):
            return None
        d={}
        i=0
        while i<len(values):
            d[self.keys[i]]=values[i]
            i+=1
        return d
    

    def toObject(self, values):                         #Convierte una lista de valores en un objeto del tipo especificado.
        if len(values) != len(self.keys):
            return None
        datos={}                                        #Diccionario nuevo para usar como '**kwargs'.
        i=0
        while i<len(values):
            valor_limpio = values[i].strip()            #Se limpian los valores (se quitan los saltos de línea).
            datos[self.keys[i].strip()] = valor_limpio
            i+=1

        obj=self.tipo_registro(**datos)                 #Se crea el objeto del tipo especificado usando '**kwargs'.
        return obj


#CLASE GENÉRICA PARA CREAR OBJETOS DE CUALQUIER TIPO SEGÚN EL '.CSV'.

class Registro(object):                               #Clase base que representa un registro genérico de la base de datos.
    def __init__(self, **kwargs):                     #'**kwargs' nos permite recibir cualquier cantidad de argumentos con nombre.
        for clave, valor in kwargs.items():
            setattr(self, clave, valor)               #Asignamos esos argumentos como atributos del objeto 'on the fly'.

    def __str__(self):                                #Representación en 'string' del objeto.
        attrb=[]
        for clave, valor in self.__dict__.items():
            attrb.append(f"{clave}: {valor}")
        clase = self.__class__.__name__               #Obtiene el nombre de la clase actual.
        return f" {clase} ( {", ".join(attrb)} )"


class Cliente(Registro):              #Clase hija de 'Registro'.

    def __init__(self, **kwargs):
        super().__init__(**kwargs)    #Llama al Constructor de la clase padre.

    def validar(self):
        
        if not hasattr(self, "nombre") or self.nombre=="" or self.nombre.isalpha()==False:
            return False

        if hasattr(self, "dni") and len(self.dni.strip()) != 8:
            return False
        
        return True
    
    def nombre_completo(self):
        if hasattr(self, "apellido"):
            return f"{self.nombre} {self.apellido}"
        return self.nombre


#CLASE GENÉRICA PARA LA LECTURA DE TODOS LOS '.CSV'.

class DB(object):

    def __init__(self, filename, tipo_registro=None):
        self.filename=filename
        self.tipo_registro=tipo_registro or Registro
    
    def read(self):
        db = []
        file = open(self.filename, "rt")
        line = file.readline()                                #se lee el encabezado (las 'keys').
        if line=="":
            return db
        keys = line.split(",")
        transforma = Transformador(keys, self.tipo_registro)  #Qué tipo  de objeto se está leyendo del '.CSV'.
        line = file.readline()                                #se lee la primer línea de 'values'.
        while line != "":
            values = line.split(",")
            obj = transforma.toObject(values)                 #Se crea el objeto del tipo especificado.
            if obj:                                           #Solo se agrega si el objeto se creó correctamente.
                db.append(obj)
            line = file.readline()
        file.close()
        return db


    def write(self, registros):
        pass


    @classmethod                                 #Método de clase para crear una DB específica para clientes.
    def crear_db_clientes(cls, filename):
        return cls(filename, Cliente)




"""
db = DB("datos_clientes2.csv")
registros = db.read()
print(registros)


i=0
while i<len(registros):
    print("Nombre: ", registros[i]["nombre"])
    i+=1
"""
