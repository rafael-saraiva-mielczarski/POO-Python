from stat import filemode


class Ingresso():
    
    def __init__(self, filme, preco, numero_poltrona, numero_ingreso, cinema, cliente, sessao):
        self._filme = filme
        self._preco = preco
        self._numero_poltrona = numero_poltrona
        self._numero_ingreso = numero_ingreso
        self._cinema = cinema
        self._cliente = cliente
        self._sessao = sessao

    def mostrar_ingresso_completo(self):
        print("Olá",{self._cliente._nome},"Voce vai assistir o filme: ",self._filme, ",na sala ",{self._sessao._numero_sala}," - ",{self._sessao._tipo}," na poltrona ",self._numero_poltrona," o numero do seu ingresso é ",self._numero_ingreso," o filme sera passado no ",{self._cinema._franquia})


