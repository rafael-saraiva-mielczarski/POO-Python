class Cliente():

    def __init__(self, cpf, nome, telefone, saldo):
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
        self._saldo = saldo

    def comprar_ingresso(ingresso):
        if Cliente.saldo >= ingresso: 
            return print ("Ingresso comprado!")
        else:
            return print("Não foi possivel comprar o ingresso, saldo insuficiente")