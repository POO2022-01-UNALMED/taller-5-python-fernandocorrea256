class Zona:
    def __init__(self, nombre, zoo=None, animales=False):
        self._nombre = nombre
        self._zoo = zoo
        self._animales = [] if not animales else animales


    # METHODS
    def agregarAnimales(self, animal):
        self._animales.append(animal)


    # SETTERS
    def setNombre(self, nombre):
        self._nombre = nombre
    
    def setZoo(self, zoo):
        self._zoo = zoo

    def setAnimales(self, animales):
        self._animales = animales

    # GETTERS
    def getNombre(self):
        return self._nombre

    def getZoo(self):
        return self._zoo

    def getAnimales(self):
        return self._animales