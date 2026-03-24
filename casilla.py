from nave import Nave  # Importa la clase Nave

class Casilla:
    def __init__(self, nave):
        # Guarda lo que hay en la casilla: 'agua' o un objeto Nave
        self.nave = nave

        # Indica si esta casilla ya fue disparada antess
        self.disparada = False

    def recibir_disparo(self):
        # Si la casilla ya había sido disparada antes
        if self.disparada == True:
            # Si la casilla contiene una nave, muestra información de esa nave
            if self.nave != 'agua':
                print(f'Casilla ya disparada con {self.nave.nombre}, de tipo {self.nave.tipo}, con {self.nave.vida} vidas')
            else:
                # Si la casilla era agua, avisa también
                print('Casilla ya disparada es de agua')
            return None

        # Si la casilla es agua y no había sido disparada antes
        if self.nave == 'agua':
            self.disparada = True
            return 0

        # Si la casilla contiene una nave y todavía no había sido disparada
        if self.disparada == False:
            # Se delega el disparo a la nave
            resultado = self.nave.recibir_disparo()

            # La casilla queda marcada como ya disparada
            self.disparada = True

            # Devuelve el resultado del disparo: tocado o hundido
            return resultado





