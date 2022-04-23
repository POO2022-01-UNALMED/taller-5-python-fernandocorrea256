class Zoologico:
    def __init__(self, nombre, ubicacion, zona=False):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zona = [] if not zona else zona

    # METHODS
    def agregarZona(self, zona):
        self._zona.append(zona)

    def cantidadTotalAnimales(self):
        if self.getZona() == None:
            return 0
        
        total = 0
        for zona in self.getZona():
            total += zona.cantidadAnimales()
        return total

    # SETTERS
    def setNombre(self, nombre):
        self._nombre = nombre

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def setZona(self, zona):
        self._zona = zona

    # GETTERS    
    def getNombre(self):
        return self._nombre

    def getUbicacion(self):
        return self._ubicacion

    def getZona(self):
        return self._zona