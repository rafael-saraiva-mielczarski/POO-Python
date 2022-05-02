class Cinema:

    def __init__(self, franquia, endereco, cliente):
        self._franquia = franquia
        self._endereco = endereco
        self._cliente = cliente

    def registrar_cliente(self, cliente):
        if cliente.cpf is not False:
            return print("Cpf valido, cliente registrado!")