from zooAnimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)

    # METHODS
    @staticmethod
    def cantidadAves():
        return len(Ave.listado)

    def movimiento():
        return "volar"

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        return Ave(nombre, edad, "monatansa", genero, "blanco y amarillo")

    # SETTERS
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas


    # GETTERS
    def getColorPlumas(self):
        return self._colorPlumas