def maiores_que_media(conteudo:dict)->list:
    media = sum(conteudo.values()) / len(conteudo)
    values = list(filter(lambda x: x[1] > media, conteudo.items()))
    values_in_order = sorted(values, key=lambda x: x[1])
    return values_in_order