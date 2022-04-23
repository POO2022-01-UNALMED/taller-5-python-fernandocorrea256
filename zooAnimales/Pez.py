from turtle import color
import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
        Pez.listado.append(self)

    # METHODS
    @staticmethod
    def cantidadPeces():
        return len(Pez.listado)

    def movimiento(self):
        return "nadar"

    @staticmethod
    def crearSalmon(nombre, edad, genero):
        Pez.salmones += 1
        return Pez(nombre, edad, "oceano", genero, "rojo", 6)

    @staticmethod
    def crearBacalao(nombre, edad, genero):
        Pez.bacalaos += 1
        return Pez(nombre, edad, "oceano", genero, "gris", 6)
    
    # SETTERS
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas


    # GETTERS
    def getColorEscamas(self):
        return self._colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas