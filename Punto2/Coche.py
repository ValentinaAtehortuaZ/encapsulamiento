class Coche:    
   
    def __init__(self):
        self.nombreEscu=None
        self.motor=None
        self.piloto=None
        self.costo=None

  #Getters
    @property
    def nombreEscu(self):
        return(self.__nombreEscu)
    @property
    def motor(self):
        return(self.__motor)
    @property
    def piloto(self):
        return (self.__piloto)
    @property
    def costo(self):
        return(self.__costo)


    #Setters
    @nombreEscu.setter
    def nombreEscu(self, nombreEscu):
        self.__nombreEscu=nombreEscu

    @motor.setter
    def motor(self, motor):
        self.__motor=motor
                
    @piloto.setter
    def piloto(self, piloto):
        self.__piloto=piloto

    @costo.setter
    def costo(self, costo):
        try:
            costov=float(costo) 
            self.__costo=costov
        except:
            print("El costo debe ser un numero")
    
       