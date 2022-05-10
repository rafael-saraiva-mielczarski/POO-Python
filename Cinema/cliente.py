class Cliente():

    def __init__(self, cpf, nome, telefone, saldo):
        self._cpf = cpf
        self._nome = nome
        self._telefone = telefone
        self._saldo = saldo

    def comprar_ingresso(self):
        if self._saldo >= 16:
            self._saldo -= 16 
            print ("Ingresso comprado!")
        else:
            print("Não foi possivel comprar o ingresso, saldo insuficiente")

    def mostrar_saldo(self):
        print(self._saldo,"R$")
