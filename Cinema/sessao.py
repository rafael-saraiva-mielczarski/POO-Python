class Sessao():
    
    def __init__(self,tipo, numero_sala, poltronas):
        self._tipo = tipo
        self._numero_sala = numero_sala
        self._poltronas = poltronas

    def mostrar_numero_de_poltronas(self):
        print(self._poltronas)