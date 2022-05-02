from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, proprietario, registro, marca, modelo, ano, cor, cavalos):
        super().__init__(proprietario, registro, marca, modelo, ano)
        self._cor = cor
        self._cavalos = cavalos
