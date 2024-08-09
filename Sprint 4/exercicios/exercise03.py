from functools import reduce
example = [
        (200,'D'),
        (300,'C'),
        (100,'C')
    ]
def calcula_saldo(lancamentos) -> float:

    valores_com_simbolo = map(lambda tupla: tupla[0] if tupla[1] == "C" else -(tupla[0]), lancamentos)
    reducer = reduce(lambda x, y: x + y, valores_com_simbolo)
    print(reducer)
    return reducer
    
calcula_saldo(example)