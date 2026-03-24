
########################################################## CLASE JUGADOR (NUEVA CLASE) ##########################################################


# jugador.py
from tablero import Tablero
from nave import Nave

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = Tablero()  # cada jugador tiene su propio tablero
        self.flota = self._obtener_flota()  # lista de naves únicas del tablero

    def _obtener_flota(self):
        """Recoge todas las naves únicas del tablero"""
        naves = set()
        for fila in self.tablero.casillero:
            for casilla in fila:
                if casilla.nave != 'agua':
                    naves.add(casilla.nave)
        return list(naves)

    def ha_perdido(self):
        """Devuelve True si todas sus naves están hundidas"""
        return all(nave.hundido for nave in self.flota)

    def mostrar_flota(self):
        for nave in self.flota:
            print(f"{nave.nombre} ({nave.tipo}) - Vida: {nave.vida} - Hundido: {nave.hundido}")