class Cinema:

    def __init__(self, franquia, endereco, cliente):
        self._franquia = franquia
        self._endereco = endereco
        self._cliente = cliente

    def registrar_cliente(self):
        if {self._cliente._cpf} == int:
            print("Cpf valido, cliente registrado!")

        else:
            print("Cliente não identificou o cpf!")