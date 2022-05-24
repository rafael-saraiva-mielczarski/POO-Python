from carro import Carro
from barco import Barco

class CarroAnfibio(Carro, Barco):
    
    def __init__(self,carro,barco):
        self._carro= carro 
        self._barco= barco

    def transciona(self):
        print("O carro anfibio transiciona de modo terreste para aquático.")

c1=Carro('123WQRW421', 4, 4, "elétrico")
b1=Barco(400, 500, "a combustão")
ca1=CarroAnfibio(c1,b1)

ca1.jogar_ancora()
ca1.acelera()
ca1.freia()
ca1.transciona()
