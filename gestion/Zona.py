from gestion.zoologico import Zoologico

class Zona:
    def __init__(self, nombre, zoo = None):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = []
        
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getZoo(self):
        return self._zoo
    
    def setZoo(self, zoo):
        self._zoo = zoo
        
    def getAnimales(self):
        return self._animales
    
    def setAnimales(self, animales):
        self._animales = animales
        
    def agregarAnimales(self, animal):
        self._animales.append(animal)
        
    def cantidadAnimales(self):
        cantidadAnimales = 0
        for _ in self._animales:
            cantidadAnimales += 1
        return cantidadAnimales
    
if __name__ == "__main__":
    zoo1 = Zoologico("Central perk", "Calle Principal")
    zona1 = Zona("salvaje", zoo1)
    zona2 = Zona("salvaje")
    ok = False
    if zona1.getNombre() == "salvaje" and zona1.getZoo().getNombre() == "Central perk" and zona2.getZoo() == None:
        ok = True
    assert(ok)
    print(ok)