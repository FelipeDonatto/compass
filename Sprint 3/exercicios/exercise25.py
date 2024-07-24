class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = "azul"
        self.capacidade = capacidade
        
a = Aviao("BOIENG456", "1500 km/h", "400")
b = Aviao("Embraer Praetor 600", "863km/h", "14")
c = Aviao("Antonov An-2", "258 Km/h", "12")
planesList = [a, b, c]
for i in planesList:
    print(f"O avião de modelo “{i.modelo}” possui uma velocidade máxima de “{i.velocidade_maxima}”, capacidade para “{i.capacidade}” passageiros e é da cor “{i.cor}”.")
