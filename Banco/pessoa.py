class Pessoa:

    def __init__(self,nome,endereco,telefone):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone


    def get_nome(self):
        return self._nome

    def set_nome(self,nome):
        self._nome = nome
    
    
    def get_endereco(self):
        return self._endereco

    def set_endereco(self,endereco):
        self._endereco = endereco


    def get_telefone(self):
            return self._telefone

    def set_telefone(self,telefone):
        self._telefone = telefone

    
        
p1 = Pessoa('Rafael Saraiva', 'Rua General Caldwell', 995124011)
print(p1.get_nome())
p1.set_nome('Roberta')
print(p1.get_nome())
