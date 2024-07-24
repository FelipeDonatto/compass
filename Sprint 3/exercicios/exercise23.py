class Calculo():
    def soma(x,y):
        print(f"Somando: {x}+{y} = {x + y}")
        return x + y
    
    def subtracao(x,y):
        print(f"Subtraindo: {x}-{y} = {x - y}")
        return x - y


Calculo.soma(4, 5)
Calculo.subtracao(4, 5)