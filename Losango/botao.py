from objeto import Objeto
from retangulo import Retangulo
from clicavel import Clicavel

class Botao(Retangulo, Clicavel):
    
    def m1(self):
        super().m1()

    def m2(self):
        super().m2()       


print(Botao.mro())

botao=Botao()
botao.m1()
botao.m2()