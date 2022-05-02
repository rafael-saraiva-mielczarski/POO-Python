from pessoa import Pessoa

class PessoaFisica(Pessoa):
    
    def __init__(self,nome, endereco, telefone, cpf, rg, estado_civil):
        super().__init__(nome, endereco, telefone)
        self._cpf = cpf
        self._rg = rg
        self._estado_civil = estado_civil

    def validar_cpf(cpf = None):
        if cpf is not None:
            return print("CPF inválido")

        return False
    
    def validar_estado_civil(estado_civil = None):
        if estado_civil is not None:
            return print("Por favor insira seu estado civil!")

        return False