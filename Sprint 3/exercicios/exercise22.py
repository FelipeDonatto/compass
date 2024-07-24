class Pessoa:
    def __init__(self, id):
        self.__nome = ''
        self.id = id
    
    @property        
    def nome(self):
        return self.__nome
        
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
