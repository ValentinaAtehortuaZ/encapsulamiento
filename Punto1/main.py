from Ciclista import Ciclista
#inicializacion de variables

i=0
ciclistas=[]

numeroCiclistas=int(input('Digite el numero de ciclistas que va a digitar: '))
     
#bucle

for i in range(numeroCiclistas):        
   
    ciclista=Ciclista()

    ciclista.name=input('Digite el nombre del ciclista: ')
    ciclista.age=input('Digite la age: ')
    ciclista.country=input('Digite el country: ')
    ciclista.time=input('Digite el time (en minutos) recorrido por el ciclista: ')

    ciclistas.append(ciclista)

#metofo/logica para recorrer la lista y mirar cual es el menor tiempo
tiempomenor=ciclistas[0].time
nombreGanador=ciclistas[0].name
for ciclista in ciclistas:
    if(ciclista.time<tiempomenor):
        tiempomenor=ciclista.time
        nombreGanador=ciclista.name    

print(f'el ganador es {nombreGanador} con un tiempo de {tiempomenor}')

