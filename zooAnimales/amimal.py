class Animal:
    _totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre 
        self._edad = edad 
        self._habitat = habitat 
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1
    
    def getNombre(self):
        return self._nombre
            
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def getEdad(self):
        return self._edad
            
    def setEdad(self, edad):
        self._edad = edad
    
    def getHabitat(self):
        return self._habitat
            
    def setHabitat(self, habitat):
        self._habitat = habitat
    
    def getGenero(self):
        return self._genero
            
    def setGenero(self, genero):
        self._genero = genero
   
    def getZona(self):
        return self._zona
            
    def setZona(self, zona):
        self._zona = zona
   
    def toString(self):
        message = f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"
        if self._zona != None:
            message += f", la zona en la que me ubico es {self._zona}, en el {self._zona._zoo}"
        return message
    
    @classmethod
    def totalPorTipo(cls):
        cantidades = {
            "Mamiferos": 0,
            "Aves": 0,
            "Reptiles": 0,
            "Peces": 0,
            "Anfibios": 0
        }

        for subclass in cls.__subclasses__():
            nameClass = subclass.__name__
            if(nameClass == "Mamifero"):
                cantidades["Mamiferos"] = subclass.cantidadMamiferos()
            elif(nameClass == "Ave"):
                cantidades["Aves"] = subclass.cantidadAves()
            elif(nameClass == "Reptil"):
                cantidades["Reptiles"] = subclass.cantidadReptiles()
            elif(nameClass == "Pez"):
                cantidades["Peces"] = subclass.cantidadPeces()
            elif(nameClass == "Anfibio"):
                cantidades["Anfibios"] = subclass.cantidadAnfibios()

        result = "\n".join([f"{k} : {v}" for k, v in cantidades.items()])
        return result