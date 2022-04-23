from animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)

    # METHODS
    @staticmethod
    def cantidadReptiles():
        return len(Reptil.listado)

    def movimiento():
        return "reptar"

    @staticmethod
    def crearIguana(nombre, edad, genero):
        Reptil.iguanas += 1
        return Reptil(nombre, edad, "humedal", genero, "verde", 3)

    @staticmethod
    def crearSerpiente(nombre, edad, genero):
        Reptil.serpientes += 1
        return Reptil(nombre, edad, "jungla", genero, "blanco", 1)


    # SETTERS
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def setLargoCola(self, largoCola):
        self._largoCola = largoCola

    # GETTERS
    def getColorEscamas(self):
        return self._colorEscamas

    def getLargoCola(self):
        return self._largoCola