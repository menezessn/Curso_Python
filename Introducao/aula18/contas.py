from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo) -> None:
        self.agencia = agencia
        self.conta = conta 
        self.saldo = saldo
    
    @abstractmethod
    def sacar (self,valor):...

    def depositar (self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO {valor})')
    
    def detalhes(self, msg = ''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('-------------')

    def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
            return f'{class_name} {attrs}'

class Poupanca(Conta):
    def sacar(self, valor): 
        valor_pos_saque = self. saldo - valor

        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print("SAQUE NEGADO")
        self.detalhes(f'SAQUE NEGADO {valor}')

class Corrente(Conta):
    def __init__(self, agencia, conta, saldo, limite) -> None:
        super().__init__(agencia,conta, saldo)
        self.limite = limite

    def sacar(self, valor): 
        valor_pos_saque = self. saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print("SAQUE NEGADO")
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'SAQUE NEGADO {valor}')

    def __repr__(self):
            class_name = type(self).__name__
            attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
            return f'{class_name} {attrs}'

    

if __name__ == '__main__':
    # cp1 = Poupanca(111,222,0)
    # cp1.sacar(1)
    # cp1.depositar(1)
    # cp1.sacar(1)
    print('##')
    cc1 = Corrente(111,222,0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(99)


