
########################################################## CLASE ATAQUE (NUEVA CLASE) ##########################################################

# ataque.py
class Ataque:
    def __init__(self, x, y, resultado=None):
        # Coordenada fila del ataque
        self.x = x

        # Coordenada columna del ataque
        self.y = y

        # Resultado del ataque:
        # 0 = agua
        # 1 = tocado
        # 2 = hundido
        self.resultado = resultado

    def __str__(self):
        # Diccionario para traducir el número del resultado a texto
        resultados = {0:"Agua", 1:"Tocado", 2:"Hundido"}

        # Devuelve una cadena legible del ataque
        return f"Ataque a ({self.x},{self.y}): {resultados.get(self.resultado, 'Pendiente')}"