class Passaro:
    def __init__(self, _voar, _emitir_som):
        self.voar = _voar
        self.emitir_som = _emitir_som

    def voando(self):
        print(self.voar)
        return self.voar

    def grasnando(self):
        print(f"{self.nome} emitindo som...")
        print(self.emitir_som)
        return self.emitir_som
    
class Pato(Passaro):
    def __init__(self, nome, _voar, _emitir_som):
        super().__init__(_voar, _emitir_som)
        self.nome = nome
        
    def especie(self):
        print(self.nome)
        return self.nome
        
class Pardal(Passaro):
    def __init__(self, nome, _voar, _emitir_som):
        super().__init__(_voar, _emitir_som)
        self.nome = nome
        
    def especie(self):
        print(self.nome)
        return self.nome        
        
a = Pato("Pato","Voando...", "Quack Quack")
a.especie()
a.voando()
a.grasnando()
b = Pardal("Pardal","Voando...", "Piu Piu")
b.especie()
b.voando()
b.grasnando()