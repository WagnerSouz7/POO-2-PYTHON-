#QUESTAO 1
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao


livro1 = Livro("Orgulho e Preconceito", "Jane Austen", "1813")
livro2 = Livro("O Alquimista", "Paulo Coelho", "1988")
livro3 = Livro("1984", "George Orwell", "1949")

print(livro1.titulo, livro1.autor,  livro1.ano_publicacao)
print(livro2.titulo, livro2.autor,  livro2.ano_publicacao)
print(livro3.titulo, livro3.autor,  livro3.ano_publicacao)

#QUEESTAO 2
class produto:
    def __init__(self, *args, **kwargs):
        if len(args) >= 1:
            self.nome = args[0]
        else:
            self.nome = kwargs.get ("Nome", "Sem Nome")
        if len(args) >= 2:
            self.preco = args[1]
        else:
            self.preco = kwargs.get("preco", 0)

    def __str__(self):
        return f'produto: {self.nome}, Preço: R${self.preco:.2f}'  
   

produto1 = produto("Notebook", 1500.00)
produto2 = produto ("Tablet")


print(produto1)
print(produto2)


#QUESTAO 3
class contaBancaria:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar (self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print ('Saldo insuficiente')
    def mostrarSaldo(self):
        print(f"Seu saldo atual é {self.saldo}")


conta1 = contaBancaria (123,'Eduardo', 5000)
conta1.depositar (200)
conta1.mostrarSaldo()
conta1.sacar (500)

conta2 = conta1
conta2.depositar(100)
conta2.mostrarSaldo()

print (conta1 is conta2)

        
