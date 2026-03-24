
########################################################## CLASE ATAQUE (NUEVA CLASE) ##########################################################

# ataque.py
class Ataque:
    def __init__(self, x, y, resultado=None):
        self.x = x
        self.y = y
        self.resultado = resultado  # 0=agua,1=tocado,2=hundido

    def __str__(self):
        resultados = {0:"Agua", 1:"Tocado", 2:"Hundido"}
        return f"Ataque a ({self.x},{self.y}): {resultados.get(self.resultado, 'Pendiente')}"