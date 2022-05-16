from Ciclista import Ciclista
#inicializacion de variables

i=0
ciclistas=[]

numeroCiclistas=int(input('Digite el numero de ciclistas que va a digitar: '))
     
#bucle

for i in range(numeroCiclistas):        
   
    ociclista=Ciclista()

    ociclista.name=input('Digite el nombre del ciclista: ')
    ociclista.age=input('Digite la age: ')
    ociclista.country=input('Digite el country: ')
    ociclista.time=input('Digite el time (en minutos) recorrido por el ciclista: ')

    ciclistas.append(ociclista)

#metofo/logica para recorrer la lista y mirar cual es el menor tiempo
tiempomenor=ciclistas[0].time
nombreGanador=ciclistas[0].name
for ciclista in ciclistas:
    if(ociclista.time<tiempomenor):
        tiempomenor=ociclista.time
        nombreGanador=ociclista.name    

print(f'el ganador es {nombreGanador} con un tiempo de {tiempomenor}')

