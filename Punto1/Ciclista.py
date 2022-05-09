class Ciclista:  

    def __init__(self):
        self.__name=None
        self.__age=None
        self.__country=None
        self.__time=None  
    
    #Getters
    @property
    def name(self):
        return(self.__name)
    @property
    def age(self):
        return(self.__age)
    @property
    def country(self):
        return (self.__country)
    @property
    def time(self):
        return(self.__time)

    #Setters
    @name.setter
    def name(self, name):
        self.__name=name

    @age.setter
    def age(self, age):
        try:
            agev=int(age)  
        
        except:
            print("La edad debe ser un numero")

        if(agev>0 and agev<150):
            self.__age=agev
        else:
            self.__age=agev=None
            print("age erronea")
            
      
    
    @country.setter
    def country(self, country):
        if(country.isnumeric()):
            self.__country=country=None
            print("Debe ser un pais gringo de mierda")
        else:
            self.__country=country

    @time.setter
    def time(self, time):
        try:
            timev=int(time) 
            self.__time=timev
        except:
            print("El time debe ser un numero")

    def guardarCiclitas(self):
        ciclista=[self.name, self.age, self.country, self.time]
        self.ciclistas.append(ciclista)
        return self.ciclistas

    def calcularTiempoMenor(self, ciclistas):
        ordenados = sorted(ciclistas, key=lambda c : c[3])
        return ordenados