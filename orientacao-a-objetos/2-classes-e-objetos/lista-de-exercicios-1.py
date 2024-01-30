# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro():
    def __init__(self):
        self.ligado = False
        self.cor = "Cinza"
        self.modelo = "Toyota"
        self.velocidade = 0
        self.velocidade_min = 0
        self.velocidade_max = 200

    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False
    
    def acelerar(self):
        if self.ligado == False:
            return
       
        self.velocidade += 10
    
    def desacelerar(self):
        if self.ligado == False:
            return
        if self.velocidade >= self.velocidade_min:
            self.velocidade -= 10

# Crie uma instância da classe carro.

meu_carro = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.

meu_carro.ligar()

for _ in range(10):
    meu_carro.acelerar()

print(f"A velocidade do carro é: {meu_carro.velocidade}")

for _ in range(5):
    meu_carro.desacelerar()

for _ in range(3):
    meu_carro.acelerar()

for _ in range(8):
    meu_carro.desacelerar()

meu_carro.desligar()

# Faça o carro "parar" utilizando os métodos da sua classe.

for _ in range(8):
    meu_carro.desacelerar()

meu_carro.desligar()

print(f"O carro é da cor {meu_carro.cor}")

 