import random

lista_aleatoria = [random.randint(0, 1000) for i in range(250)]

animais = sorted(["Cachorro", "Gato", "Elefante", "Girafa", "Tigre", "Leão", "Cavalo", "Rinoceronte", 
           "Coelho", "Macaco", "Panda", "Cobra", "Urso", "Golfinho", "Tartaruga", "Coruja", 
           "Camelo", "Hipopótamo", "Pinguim", "Águia", "Jacaré", "Lobo", "Raposa", "Zebra", 
           "Baleia", "Canguru", "Vaca", "Ovelha", "Porco", "Gorila"], reverse=True)

animais_aleatorios = [print(i) for i in animais]

file = open(f"./animais.csv", "w")
file.write("Animal\n")
for i in animais:
    file.write(f"{i}\n")