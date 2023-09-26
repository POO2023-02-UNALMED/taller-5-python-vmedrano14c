from zooAnimales.animal import Animal

class Pez(Animal):
    salmones = 0
    bacalaos = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas = None, cantidadAletas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas 
        self._cantidadAletas = cantidadAletas
        self._listado.append(self)
        
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
        
    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas
        
    def getListado(self):
        return self._listado
    
    def setListado(self, listado):
        self._listado = listado
        
    def cantidadPeces():
        return len(Pez._listado)
    
    @staticmethod
    def crearSalmon(nombre, edad, genero):
        colorEscamas = "rojo"
        cantidadAletas = 6
        habitat = "oceano"
        Pez(nombre, edad, habitat, genero, colorEscamas, cantidadAletas)
        Pez.salmones += 1
        
    @staticmethod
    def crearBacalao(nombre, edad, genero):
        colorEscamas = "gris" 
        cantidadAletas = 6
        habitat = "oceano"
        Pez(nombre, edad, habitat, genero, colorEscamas, cantidadAletas)
        Pez.bacalaos += 1