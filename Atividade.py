#Questão 01 - Wagner Isaquiel Pedro de Souza - 01743816
class animal:
    def __init__(self, nome):
        self.nome = nome
    
    def som(self):
        print("Som Génerico")
    
        
class cachorro(animal):
    def som(self):
        print("Au Au")
        
class gato(animal):
    def som(self):
        print("Miau Miau")
        
cachorro1 = cachorro("Husky")
gato1 = gato("Siamês")

cachorro1.som()
gato1.som()

#Questão 02 - Wagner Isaquiel Pedro de Souza - 01743816


# class veiculo:
#     def __init__(self, velocidade_maxima):
#         self._velocidade_maxima = 120

#     def get_velocidade_maxima(self):
#         return self._velocidade_maxima

#     def acelerar(self, valor):
#         Velocidade = self.get_velocidade_maxima() + valor
#         if Velocidade > 200:
#             self._velocidade_maxima = 200
#         else:
#             self._velocidade_maxima = Velocidade

# veiculo = veiculo1()
# print(veiculo.get_velocidade_maxima())

# veiculo.acelerar(100)
# print(veiculo.get_velocidade_maxima()) #Deve sair 200, porque o limite é 200.

class Veiculo:
    def __init__(self, velocidade_maxima):
        self._velocidade_maxima = velocidade_maxima 
    def get_velocidade_maxima(self):
        return self._velocidade_maxima

    def acelerar(self, valor):
        nova_velocidade = self.get_velocidade_maxima() + valor
        if nova_velocidade > 180:
            self._velocidade_maxima = 180
        else:
            self._velocidade_maxima = nova_velocidade

class Carro(Veiculo):
    def frear(self, valorf):
        frenagem = self.get_velocidade_maxima() - valorf
        if frenagem < 0:
            self._velocidade_maxima = 0
        else:
            self._velocidade_maxima = frenagem


carro1 = Carro(120)
print(carro1.get_velocidade_maxima()) 
carro1.acelerar(70)
print(carro1.get_velocidade_maxima())  
carro1.frear(50)
print(carro1.get_velocidade_maxima())  

#Questão 03 - Carlos Eduardo da Costa Souza - 01717953

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.__saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > self.__saldo:
            print("Saldo insuficiente para o saque.")
        elif valor <= 0:
            print("O valor do saque deve ser positivo.")
        else:
            self.__saldo -= valor

    def ver_saldo(self):
        return self.__saldo


class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo_inicial=0, taxa_juros=0.01):
        super().__init__(saldo_inicial)  
        self.taxa_juros = taxa_juros

    def aplicar_juros(self):
        saldo_atual = self.ver_saldo()
        juros = saldo_atual * self.taxa_juros
        self.depositar(juros)



conta = ContaPoupanca(saldo_inicial=5000, taxa_juros=0.02)

conta.depositar(400)
print(f"Saldo após o depósito: R$ {conta.ver_saldo():.2f}")

conta.sacar(500)
print(f"Saldo depois do saque: R$ {conta.ver_saldo():.2f}")

conta.aplicar_juros()
print(f"Saldo após aplicar os juros: R$ {conta.ver_saldo():.2f}")

#Questão 04 - Carlos Eduardo da Costa Souza - 01717953

class Conta:
    def __init__(self, saldo_inicial=0, limite=1000):
        self.__saldo = saldo_inicial 
        self._limite = limite  

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > (self.__saldo + self._limite):
            print("Saldo e limite insuficientes.")
        else:
            self.__saldo -= valor

    def ver_saldo(self):
        return self.__saldo

    def ver_limite(self):
        return self._limite


class ContaEspecial(Conta):
    def __init__(self, saldo_inicial=0, limite=2000):
        super().__init__(saldo_inicial, limite)

    def sacar(self, valor):
        if valor > (self.ver_saldo() + 2 * self._limite):
            print("Saque não permitido, excedeu o limite.")
        else:
            super().sacar(valor)



conta_comum = Conta(saldo_inicial=500, limite=1000)
conta_comum.depositar(300)
print(f"Saldo conta comum: R$ {conta_comum.ver_saldo():.2f}")
conta_comum.sacar(1500)
print(f"Saldo depois do saque conta comum: R$ {conta_comum.ver_saldo():.2f}")

conta_especial = ContaEspecial(saldo_inicial=500, limite=2000)
conta_especial.depositar(500)
print(f"Saldo da conta especial: R$ {conta_especial.ver_saldo():.2f}")
conta_especial.sacar(3500)
print(f"Saldo após saque da conta especial: R$ {conta_especial.ver_saldo():.2f}")


