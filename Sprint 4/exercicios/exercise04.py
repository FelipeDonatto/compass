operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

def calcular_valor_maximo(operadores,operandos) -> float:
    values = list(map(lambda equacao: eval(f"{equacao[1][0]} {equacao[0]} {equacao[1][1]}"), list(zip(operadores,operandos))))
    print(max(values))
    return max(values)
    
    
calcular_valor_maximo(operadores,operandos)    
    
