class Barco():
    
    def __init__(self, capacidade , tamanho, motor):
        self._capacidade = capacidade 
        self._tamanho = tamanho
        self._motor = motor

    def jogar_ancora(self):
        print("O barco joga sua ancora e fica parado")

    def acelera(self):
        print("O barco acelera no mar.")