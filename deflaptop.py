#Def function
def laptop_nuvo(ram, cpu, antivrus = False):
    
    print("Il laptop avra le seguenti caratteristiche:")
    print("RAM: " + ram)
    print("CPU: " + cpu)
    if antivrus == True:
        print("Hai comprato anche un antivirus!")
    else:
        print("Non hai comprato antivirus")

laptop_nuvo("8GB", "i8", antivrus=False) 

def potenza_lap(wat_computer):
    
    if wat_computer >= 20 and wat_computer <= 30:
        print("Hai un computer discreto.")
    elif wat_computer <= 10 and wat_computer >= 3 :
        print("Hai un computer scarso.")
    else:
        print("Hai un buon computer.")
    return wat_computer
        
potenza_lap(80)
