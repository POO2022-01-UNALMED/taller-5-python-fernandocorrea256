class Animal:
    totalAnimales = 0
    def __init__(self, nombre, edad, habitat, genero, zona=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal.totalAnimales += 1

    # METHODS
    def movimiento(self):
        return "desplazarse"

    @staticmethod
    def totalPorTipo():
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil

        return f"""Mamiferos: {Mamifero.cantidadMamiferos()}
        Aves: {Ave.cantidadAves()}
        Reptiles: {Reptil.cantidadReptiles()}
        Peces: {Pez.cantidadPeces()}
        Anfibios: {Anfibio.cantidadAnfibios()}"""

    def __str__(self):
        if (self._zona):
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}, la zona en la que me ubico es {self.getZona()}, en el {self.getZona().getZoo()}" 
        else:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}"


    # SETTERS
    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    def setHabitat(self, habitat):
        self._habitat = habitat

    def setGenero(self, genero):
        self._genero = genero

    def setZona(self, zona):
        self._zona = zona

    # GETTERS
    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def getHabitat(self):
        return self._habitat

    def getGenero(self):
        return self._genero

    def getZona(self):
        return self._zona