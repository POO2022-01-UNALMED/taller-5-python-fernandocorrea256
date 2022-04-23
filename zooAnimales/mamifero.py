from zooAnimales.animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)

    # METHODS
    @staticmethod
    def cantidadMamiferos():
        return len(Mamifero.listado)

    @staticmethod
    def crearCaballo(nombre, edad, genero):
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, "pradera", genero, True, 4)

    @staticmethod
    def crearLeon(nombre, edad, genero):
        Mamifero.leones += 1
        return Mamifero(nombre, edad, "selva", genero, True, 4)

    # SETTERS
    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def setPatas(self, patas):
        self._patas = patas

    # GETTERS
    def isPelaje(self):
        return self._pelaje
    
    def getPatas(self):
        return self._patas