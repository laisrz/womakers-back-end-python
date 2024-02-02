# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela 
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança", "propriedades", "encapsulamento" e "classe abstrata".
from abc import ABC, abstractmethod
class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self._nome = nome
        self._telefone = telefone
        self._renda_mensal = renda_mensal

class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
        self.cheque_especial = renda_mensal



# A classe base da conta corrente
class BaseContaCorrente(ABC):
    def __init__(self, saldo, titular):
        self.saldo = saldo
        self.titular = titular
        self.operações = []

    @abstractmethod
    def saque(self):
        pass
        

    @abstractmethod
    def deposito(self):
        pass

class ContaCorrente(BaseContaCorrente):
    def __init__(self, saldo, titular):
        super().__init__(saldo, titular)
    
    def saque(self, saque_valor):

        # saque no caso de cliente mulher
        if self.titular == ClienteMulher:
            if self.saldo + ClienteMulher.cheque_especial > saque_valor:
                self.saldo -= saque_valor
                self.operações.append("saque")
                print(f"Saque realizado no valor de {saque_valor}. O saldo da conta corrente atual é {self.saldo}")
            else:
                raise ValueError(f'Não há saldo suficiente na conta corrente') 
            
        # saque no caso de cliente homem
        elif self.saldo > saque_valor:
            self.saldo -= saque_valor
            self.operações.append("saque")
            print(f"Saque realizado no valor de {saque_valor}. O saldo da conta corrente atual é {self.saldo}")
        else:
            raise ValueError(f'Não há saldo suficiente na conta corrente')

    def deposito(self, deposito_valor):
            
        self.saldo += deposito_valor
        self.operações.append("depósito")
        print(f"Depósito no valor de {deposito_valor}. O saldo atual da conta corrente é de {self.saldo}")



Nicole = ClienteMulher("Nicole", 1197345632, 10000)

contaNicole = ContaCorrente(2000, Nicole)

Fernando = Cliente("Fernando", "1145468734", 3000)
contaFernando = ContaCorrente(2000, Fernando)
contaFernando.saque(100)
contaFernando.deposito(3000)
contaNicole.saque(4000)

contaNicole.deposito(200)





