
from tablero import Tablero  # Importa la clase Tablero para crear el tablero del juegoo

class Juego:
    def __init__(self):
        # Crea una instancia del tablero
        self.tablero = Tablero()

        # Lanza varios ataques de prueba al iniciar el juego
        self.lanzar_ataque(1, 0)
        self.lanzar_ataque(1, 0)
        self.lanzar_ataque(1, 1)
        self.lanzar_ataque(1, 2)
        self.lanzar_ataque(2, 1)
        self.lanzar_ataque(1, 4)

    def mostrar_resultado(self, resultado):
        # Muestra por pantalla el resultado del disparo según el valor recibido
        if resultado == 0:
            print("Agua")
        elif resultado == 1:
            print("Tocado")
        elif resultado == 2:
            print("Hundido")

    def lanzar_ataque(self, x, y):
        # Muestra las coordenadas a las que se dispara
        print(f"Ataque a {x},{y}")

        # Accede a la casilla concreta del tablero usando fila y columna
        casilla = self.tablero.casillero[x][y]

        # Llama al método de la casilla para procesar el disparo
        resultado = casilla.recibir_disparo()

        # Si el resultado no es None, significa que el disparo sí produce un resultado válido
        # None ocurre cuando la casilla ya había sido disparada antes
        if resultado is not None:
            self.mostrar_resultado(resultado)

# Crea y ejecuta el juego
juego = Juego()




'''
########################################################## CLASE JUEGO UPGRADEADA ##########################################################

# juego.py
from zJugador import Jugador
from zAtaque import Ataque

class Juego:
    def __init__(self):
        # Crear dos jugadores con su tablero y flota
        self.jugador1 = Jugador("Player1")
        self.jugador2 = Jugador("Player2")
        self.historial = []  # Guarda ataques de ambos jugadores

        # Ataques de ejemplo al jugador1
        self.lanzar_ataque(self.jugador1, 1, 0)
        self.lanzar_ataque(self.jugador1, 1, 1)

        # Ataques de ejemplo al jugador2
        self.lanzar_ataque(self.jugador2, 0, 0)
        self.lanzar_ataque(self.jugador2, 1, 2)

        # Mostrar estado final de la flota de ambos jugadores
        print("\nEstado final de la flota Jugador1:")
        self.jugador1.mostrar_flota()

        print("\nEstado final de la flota Jugador2:")
        self.jugador2.mostrar_flota()

        # Mostrar historial de ataques
        print("\nHistorial de ataques:")
        for ataque in self.historial:
            print(ataque)

    def lanzar_ataque(self, jugador, x, y):
        """Ataca la casilla (x,y) del tablero del jugador"""
        print(f"\nAtacando coordenadas ({x},{y}) en {jugador.nombre}")
        casilla = jugador.tablero.casillero[x][y]
        resultado = casilla.recibir_disparo()  # 0=Agua, 1=Tocado, 2=Hundido

        # Guardar ataque en historial
        ataque = Ataque(x, y, resultado)
        self.historial.append(ataque)

        # Mostrar resultado en pantalla
        if resultado == 0:
            print("Resultado: Agua")
        elif resultado == 1:
            print("Resultado: Tocado")
        elif resultado == 2:
            print(f"Resultado: Hundido - {casilla.nave.nombre}")
        else:
            # Caso de casilla ya disparada
            if casilla.nave != 'agua':
                print(f"Casilla ya disparada con {casilla.nave.nombre}, vida restante: {casilla.nave.vida}")
            else:
                print("Casilla ya disparada (Agua)")

# Ejecutar juego
if __name__ == "__main__":
    juego = Juego()

'''