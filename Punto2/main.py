from Coche import Coche
escuderia=[]
escuderias=[]
opcion=0
while(opcion!=5):
    print("__________________________________")
    print("              Menú                ")
    print("__________________________________")
    print("1--> Registrar escuderia. ")
    print("2--> Mostrar escuderia mas cara. ")
    print("3--> Mostrar cuantas tienen mercedes, ferrari y cuantas renault")
    print("4--> Buscar y eliminar producto. ")
    print("5--> SALIR ")
    print("__________________________________")

    opcion=int(input("Digite la opción deseada: "))
    print("__________________________________")

    if(opcion==1):
        try:
            ocoche=Coche()
            print("ESCUDERIA")
            ocoche.nombreEscu=input("Digite el nombre de la escuderia: ")
            ocoche.motor=input("Digite el motor: (Mercedes/Ferrari/Renault/Honda)")
            ocoche.piloto=input("Digite el nombre del piloto: ")
            ocoche.costo=input("Digite el costo anual de la escuderia: ")

            escuderia=[ocoche.nombreEscu,ocoche.motor,ocoche.piloto,ocoche.costo]
            escuderias.append(escuderia)
        except:
            print("No se guardo la escuderia") 

    elif(opcion==2):
        ordenados = sorted(escuderias, key=lambda escuderia : escuderia[3], reverse=True)
        print(f"La escuderia mas cara es: {ordenados}")

    elif(opcion==3):
        mercedes = len(list(filter(lambda escuderia: escuderia[1]=="mercedes",escuderias)))
        ferrari = len(list(filter(lambda escuderia: escuderia[1]=="ferrari",escuderias)))
        renault = len(list(filter(lambda escuderia: escuderia[1]=="renault",escuderias)))
        honda = len(list(filter(lambda escuderia: escuderia[1]=="honda",escuderias)))
    
        totalEscuderias={'mercedes':mercedes, 'ferrari':ferrari, 'renault': renault, 'honda': honda}
        print(f'El inventario esta distribuido de la siguiente manera: {totalEscuderias}')
    elif(opcion==5):
        print("Gracias por preferirnos")

    else:
        print("Ingrese una opcion valida")