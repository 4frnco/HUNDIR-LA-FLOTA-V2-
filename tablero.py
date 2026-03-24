
from casilla import *  # Importa Casilla y Nave

class Tablero:
    def __init__(self, tamanho=10):
        self.AGUA = 0
        self.TOCADO = 1
        self.HUNDIDO = 2

        # Creación de las distintas naves
        por1 = Nave("Manuel", "portaaviones", 5)
        fra1 = Nave("Damián", "fragata", 3)
        fra2 = Nave("Elena", "fragata", 3)
        fra3 = Nave("Noelia", "fragata", 3)
        sub1 = Nave("U-47", "submarino", 1)
        sub2 = Nave("U-96", "submarino", 1)
        sub3 = Nave("U-505", "submarino", 1)
        sub4 = Nave("U-534", "submarino", 1)

        # Matriz 10x10 tal como la definiste
        self.casillero = [
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla(por1), Casilla(por1), Casilla(por1), Casilla(por1), Casilla(por1), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla(fra1), Casilla(fra1), Casilla(fra1), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla(sub1), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla(fra2), Casilla(fra2), Casilla(fra2), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla(fra3), Casilla(fra3), Casilla(fra3), Casilla('agua'), Casilla('agua'), Casilla(sub3), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua')],
            [Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla(sub4), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla('agua'), Casilla(sub2)]
        ]

    def comprobar_impacto(self, x, y):
        """
        Función de debug: comprueba si hay nave en la casilla (x,y) y procesa disparo.
        Devuelve AGUA, TOCADO, HUNDIDO o None si ya fue disparada.
        """
        casilla = self.casillero[x][y]
        print(f"[LOG] Comprobando impacto en casilla ({x},{y})")

        resultado = casilla.recibir_disparo()

        if resultado is None:
            print(f"[LOG] Casilla ({x},{y}) ya fue disparada")
        elif resultado == self.AGUA:
            print(f"[LOG] Agua en ({x},{y})")
        elif resultado == self.TOCADO:
            print(f"[LOG] {casilla.nave.nombre} Tocado en ({x},{y})")
        elif resultado == self.HUNDIDO:
            print(f"[LOG] {casilla.nave.nombre} Hundido en ({x},{y})")

        return resultado