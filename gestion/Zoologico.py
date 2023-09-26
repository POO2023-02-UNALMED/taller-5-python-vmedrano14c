class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion: ubicacion
        self._zonas = []
        
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
        
    def getZona(self):
        return self._zonas
    
    def setZonas(self, zonas):
        self._zonas = zonas
        
    def agregarZonas(self, zona):
        self._zonas.append(zona)
    
    def cantidadTotalAnimales(self):
        totalAnimales = 0
        for zona in self._zonas:
            totalAnimales += zona.cantidadAnimales()
        return totalAnimales
        
if __name__ == "__main__":
    zoo = Zoologico("Central park", "Calle Principal")
    ok = False
    if(zoo.getNombre() == "Central park"):
        ok = True
    assert(ok)
    print(ok)