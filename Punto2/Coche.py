class Coche:    
   
    def __init__(self,escuderias):
        self.escuderias=escuderias
        
    def calcularMasCara(self):
        ordenados = sorted(self.escuderias, key=lambda escuderia : escuderia[3], reverse=True)
        return ordenados[0]

    def contarEscuderias(self):
        i=0
        mercedes=0
        ferrari=0
        renault=0
        honda=0
        for i in range(len(self.escuderias)):
            if(self.escuderias[i][1]=='mercedes'):
                mercedes+=1
            elif(self.escuderias[i][1]=='ferrari'):
                ferrari+=1
            elif(self.escuderias[i][1]=='renault'):
                renault+=1
            elif(self.escuderias[i][1]=='honda'):
                honda+=1

        totalEscuderias={'mercedes':mercedes, 'ferrari':ferrari, 'renault': renault, 'honda': honda}
        return totalEscuderias
