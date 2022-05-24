class Carro():
    
    def __init__(self, placa, rodas, numero_portas, motor):
        self._placa = placa
        self._rodas = rodas
        self._numero_portas = numero_portas
        self._motor = motor

    def acelera(self):
        print("O carro é acelerado.")

    def freia(self):
        print("O carro é freiado.")