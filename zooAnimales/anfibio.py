from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio.listado.append(self)

    # METHODS
    @staticmethod
    def cantidadAnfibios():
        return len(Anfibio.listado)

    def movimiento():
        return "saltar"

    @staticmethod
    def crearRana(nombre, edad, genero):
        Anfibio.ranas += 1
        return Anfibio(nombre, edad, "selva", genero, "rojo", True)

    @staticmethod
    def crearSalamandra(nombre, edad, genero):
        Anfibio.salamandras += 1
        return Anfibio(nombre, edad, "selva", genero, "negro y amarillo", False)

    # SETTERS
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    # GETTERS
    def getColorPiel(self):
        return self._colorPiel

    def isVenenoso(self):
        return self._venenoso