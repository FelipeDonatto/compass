class Lampada:
    def __init__(self, _ligada):
        self.ligada = _ligada

    def liga(self):
        self.ligada = True
        return self.ligada
    
    def desliga(self):
        self.ligada = False
        return self.ligada

    def esta_ligada(self):
        return self.ligada


Lampada.liga(Lampada)
Lampada.esta_ligada(Lampada)
Lampada.desliga(Lampada)
Lampada.esta_ligada(Lampada)