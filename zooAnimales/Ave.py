from zooAnimales.Animal import Animal

class Ave(Animal):
    halcones = 0
    aguilas = 0
    _listado = []
    def __init__(self, nombre, edad, habitat, genero, colorPlumas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        self._listado.append(self)
        
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
        
    def getListado(self):
        return self._listado
    
    def setListado(self, listado):
        self._listado = listado
    
    @staticmethod
    def cantidadAves():
        return len(Ave._listado)
    
    @staticmethod
    def crearHalcon(nombre, edad, genero):
        colorPlumas = "cafe glorioso" 
        habitat = "montanas"
        Ave(nombre, edad, habitat, genero, colorPlumas)
        Ave.halcones += 1
        
    @staticmethod
    def crearAguila(nombre, edad, genero):
        colorPlumas = "blanco y amarillo" 
        habitat = "montanas"
        Ave(nombre, edad, habitat, genero, colorPlumas)
        Ave.aguilas += 1