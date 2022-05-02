from veiculo import Veiculo

class Aviao(Veiculo):

    def __init__(self, proprietario, registro, marca, modelo, ano, companhia_aerea, motor):
        super().__init__(proprietario, registro, marca, modelo, ano)
        self._companhia_aerea = companhia_aerea
        self._motor = motor