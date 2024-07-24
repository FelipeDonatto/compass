palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'];

for palavra in palavras:
    count = 0
    index = 0
    for letra in palavra:
        if letra == palavra[(len(palavra) - 1) - index]:
            count += 1
        index += 1
    if count != len(palavra):
        print(f"A palavra: {palavra} não é um palíndromo")
    else:
        print(f"A palavra: {palavra} é um palíndromo")