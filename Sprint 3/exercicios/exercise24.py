class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
    
    def ordenacaoCrescente(self): 
        ascList = sorted(self.listaBaguncada, reverse=False) 
        print(ascList)
        return ascList
    def ordenacaoDecrescente(self):
        descList = sorted(self.listaBaguncada, reverse=True) 
        print(descList)
        return descList
        
crescente = Ordenadora([3,4,2,1,5])
crescente.ordenacaoCrescente()
decrescente =  Ordenadora([9,7,6,8])
decrescente.ordenacaoDecrescente()
