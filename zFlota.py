
########################################################## CLASE FLOTA (NUEVA CLASE) ##########################################################

# flota.py
class Flota:
    def __init__(self, naves=None):
        self.naves = naves if naves else []

    def agregar_nave(self, nave):
        if nave not in self.naves:
            self.naves.append(nave)

    def todas_hundidas(self):
        return all(nave.hundido for nave in self.naves)

    def mostrar_estado(self):
        for nave in self.naves:
            estado = "Hundido" if nave.hundido else "Tocado" if nave.vida < nave.vida_max else "Intacto"
            print(f"{nave.nombre} ({nave.tipo}) - {estado} - Vida: {nave.vida}")