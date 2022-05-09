from Coche import Coche
escuderia=[]
escuderias=[]
opcion=0
while(True):

    print("__________________________________")
    print("              Menú                ")
    print("__________________________________")
    print("1--> Registrar escuderia. ")
    print("2--> Mostrar escuderia mas cara. ")
  #  print("3--> Mostrar cuantas tienen mercedes, ferrari y cuantas renault")
    print("4--> Buscar y eliminar producto. ")
    print("0--> SALIR ")
    print("__________________________________")

    opcion=int(input("Digite la opción deseada: "))
    print("__________________________________")

    if(opcion==1):
        print("ESCUDERIA")
        nombreEscu=input("Digite el nombre de la escuderia: ")
        motor=input("Digite el motor: (Mercedes/Ferrari/Renault/Honda)")
        piloto=input("Digite el nombre del piloto: ")
        costo=int(input("Digite el costo anual de la escuderia: "))

        escuderia=[nombreEscu,motor,piloto,costo]
        escuderias.append(escuderia)
        
    elif(opcion==2):
        ocoche=Coche(escuderias)
        print(f"La escuderia mas cara es: {ocoche.calcularMasCara()}")

    elif(opcion==3):
        print(f'El inventario esta distribuido de la siguiente manera: {ocoche.contarEscuderias()}')

    elif(opcion==0):
        False