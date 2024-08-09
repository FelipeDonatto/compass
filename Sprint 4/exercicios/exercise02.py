def conta_vogais(texto:str)-> int:
    texto_lista = list(texto)
    vogais = list(filter(lambda x: x in ["a", "e", "i", "o", "u","A", "E", "I","O", "U"], texto_lista))
    vogais_string = ''.join(str(e) for e in vogais)

    print(len(vogais_string))
    return (len(vogais_string))
    