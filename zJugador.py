
########################################################## CLASE JUGADOR (NUEVA CLASE) ##########################################################

# jugador.py
from tablero import Tablero
from nave import Nave

class Jugador:
    def __init__(self, nombre):
        # Nombre del jugador
        self.nombre = nombre

        # Cada jugador tiene su propio tablero
        self.tablero = Tablero()

        # Guarda una lista de naves únicas del tablero
        self.flota = self._obtener_flota()

    def _obtener_flota(self):
        """Recoge todas las naves únicas del tablero"""
        naves = set()

        # Recorre todas las filas del tablero
        for fila in self.tablero.casillero:
            # Recorre todas las casillas de cada fila
            for casilla in fila:
                # Si la casilla no es agua, añade la nave al conjunto
                # Se usa set para evitar repetir la misma nave varias veces
                if casilla.nave != 'agua':
                    naves.add(casilla.nave)

        # Convierte el conjunto en lista y lo devuelve
        return list(naves)

    def ha_perdido(self):
        """Devuelve True si todas sus naves están hundidas"""
        return all(nave.hundido for nave in self.flota)

    def mostrar_flota(self):
        # Recorre la flota y muestra el estado actual de cada nave
        for nave in self.flota:
            print(f"{nave.nombre} ({nave.tipo}) - Vida: {nave.vida} - Hundido: {nave.hundido}")