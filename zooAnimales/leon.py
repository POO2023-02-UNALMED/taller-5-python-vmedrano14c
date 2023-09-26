from zooAnimales.animal import Animal

class Mamifero(Animal):
    caballos = 0
    leones = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, pelaje = False, patas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje 
        self._patas = patas
        self._listado.append(self)
        
    def isPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje
        
    def getPatas(self):
        return self._patas
    
    def setPatas(self, patas):
        self._patas = patas
        
    def getListado(self):
        return self._listado
    
    def setListado(self, listado):
        self._listado = listado
    
    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero._listado)
    
    @staticmethod
    def crearCaballo(nombre, edad, genero):
        pelaje = True
        patas = 4
        habitat = "pradera"
        Mamifero(nombre, edad, habitat, genero, pelaje, patas)
        Mamifero.caballos += 1
        
    @staticmethod
    def crearLeon(nombre, edad, genero):
        pelaje = True
        patas = 4
        habitat = "selva"
        Mamifero(nombre, edad, habitat, genero, pelaje, patas)
        Mamifero.leones += 1