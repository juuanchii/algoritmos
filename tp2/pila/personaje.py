class Personaje:

    def __init__(self, nombre: str, c_pelis: int):
        self._nombre = nombre
        self._c_pelis = c_pelis

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getCantPelis(self):
        return self._c_pelis
    
    def setCantPelis(self, c_pelis: int):
        self._c_pelis = c_pelis