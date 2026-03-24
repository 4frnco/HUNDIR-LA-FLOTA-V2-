class Nave:
    def __init__(self, nombre, tipo, vida):
        # Nombre concreto de la nave
        self.nombre = nombre

        # Tipo de nave: portaaviones, fragata, submarino...
        self.tipo = tipo

        # Vida actual de la navee
        self.vida = vida

        # Indica si ya está hundida o no
        self.hundido = False

        # Constantes de resultado
        self.TOCADO = 1
        self.HUNDIDO = 2

    def recibir_disparo(self):
        # Si la nave ya estaba hundida, devuelve directamente HUNDIDO
        if self.hundido:
            return self.HUNDIDO

        # Si no estaba hundida, pierde una vida
        self.vida -= 1

        # Si la vida llega a 0 o menos, la nave se marca como hundida
        if self.vida <= 0:
            self.hundido = True
            print(f"{self.nombre} hundido")
            return self.HUNDIDO
        else:
            # Si aún le queda vida, está tocada pero no hundida
            print(f"{self.nombre} tocado. Vida restante: {self.vida}")
            return self.TOCADO