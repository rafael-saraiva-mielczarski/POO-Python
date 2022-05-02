from veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, proprietario, registro, marca, modelo, ano, cor, cc):
        super().__init__(proprietario, registro, marca, modelo, ano)
        self._cor = cor
        self._cc = cc