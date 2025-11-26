#HELPER

class Transformador(object):

    def __init__(self, attrb):
        self.keys=attrb
    
    def csv2dict(self, values):
        if len(values) != len(self.keys):
            return None
        d={}
        i=0
        while i<len(values):
            d[self.keys[i]]=values[i]
            i+=1
        return d
    

class DB(object):

    def __init__(self, filename):
        self.filename=filename
    
    def read(self):
        db = []
        file = open(self.filename, "rt")
        line = file.readline().rstrip("\n")
        if line=="":
            return db
        keys = line.split(",")
        transforma = Transformador(keys)
        line = file.readline()
        while line != "":
            values = line.split(",")
            d = transforma.csv2dict(values)
            db.append(d)
            line = file.readline()
        file.close()
        return db

##############################################################################

def dict2csv(vector):
        
    keys=list(vector[0].keys())
    csv=""
    i=0
    while i<len(keys):
        if i != 0:
            csv+=","
        csv+=keys[i]
        i+=1
    csv+="\n"
    
    i=0
    while i<len(vector):
        x=0
        while x<len(keys):
            if x != 0:
                csv+=","
            csv=csv + str(vector[i][keys[x]]).strip()
            x+=1
        csv+="\n"
        i+=1
    
    filename=input("Nombre su nuevo archivo '.CSV' (o deje el campo VACÍO y presione ENTER para retroceder): ")
    if filename=="":
        return None
    filename+=".csv"
    file=open(filename, "w")
    file.write(csv)
    file.close()
