from pessoa import Pessoa
from agencia import Agencia

class ContaCorrente:
    
    def __init__(self, numero_cc, saldo, agencia, pessoa):
        self._numero_cc = numero_cc
        self._saldo = saldo
        self._agencia = agencia
        self._pessoa = pessoa

p1 = Pessoa('Rafael Saraiva', 'Rua General Caldwell', 995124011)
a1 = Agencia(1001, 32310285 , 'Borges de Medeiros')
cc1 = ContaCorrente(42, 100000, a1, p1)

print(cc1._pessoa._nome)