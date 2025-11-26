import csv

def sincronizar(slots, turnos):

    with open(turnos, "r") as turnos_csv:
        x=csv.DictReader(turnos_csv)
        
        with open(slots, "r") as slots_csv:
            z= list(csv.DictReader(slots_csv))
            
            for line_x in x:
                for line_z in z:
                    if line_x["date"] == line_z["date"]:
                        if line_x["time"] == line_z["time"]:
                            z.remove(line_z)
                    
            with open(slots, "w", newline="") as slots_ow:
                keys=["date", "time"]
                o=csv.DictWriter(slots_ow, fieldnames=keys)
                o.writeheader()
                for line in z:
                    o.writerow(line)

if __name__=="__main__":
    sincronizar("espacios_libres_PRB.csv", "")
