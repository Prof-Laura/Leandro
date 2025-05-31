## Métodos úteis da classe string - str()

nome = 'Laura'
nome2 = "Leandro"

print(len(nome))    # len() - retorna o tamanho da string

for letra in nome2:
    print(letra)

print(nome[4])
print(nome2[0])
print(nome[-2])

# Fatiamento
# É uma técnica usada para retornar substrings. Para fatiar informamos início (inclusivo), o fim (exclusivo) e o passo.
print(nome2[:6])    # Aqui o pyhton entende que o início deve ser 0 e o passo 1
print(nome2[2:])    # Aqui o python entende que o fim deve ser o tamanho da string
print(nome2[3:6])   # Início e fim. O python entende que o passo é 1
print(nome2[0:5:2]) # Início, fim e step
print(nome2[:])     # Retorna a string inteira
print(nome2[::])    # Retorna a string inteira
print(nome2[::-1])  # Inverte a string, o que chamamos de espelhamento
print(nome2[-1:-6]) # Retorna um string vazia, pois o fatiamento padrão vai da esquerda para a direita
print(nome2[-1:-8:-1])  # Retorna a string espelhada. Repare que é necessário ter início como -1, pois o 0 é inválido nesse caso, e o final precisa ser o tamanho da string+1, pois contamos do 1 até o final agora. 

# Upper, lower e title
curso = 'pYtHoN cUrSo'
print(curso.upper())    # Deixa tudo maiúsculo
print(curso.lower())    # Deixa tudo minúsculo
print(curso.title())    # Deixa letra inicial de cada palavra em maiúsculo

# strip, lstrip e rstrip
curso = '      Python      '
print(curso.strip() + ".")  # Retira os espaços em branco da direita e esquerda
print(curso.lstrip() + ".") # Retira os espaços em branco da esquerda
print(curso.rstrip() + ".") # Retira os espaços em branco da direita

# center, join e multiplicação de string
curso = 'Python'
print(curso*3)  # Repete a string 3 vezes
print(curso.center(10, "*"))    # Centraliza a palavra preenchendo o resto dos espaços com *. O total de caracteres com o * deve ser 10.
print("_".join(curso))  # Coloca o _ entre cada letra da string

# replace e find
frase = 'Hoje levei um pão com queijo e presunto'

nova_frase = frase.replace('presunto', 'mortadela') # Substitui a primeira palavra pela segunda
print(nova_frase)

encontrou = nova_frase.lower().find('hoje') # Retorna o índice da primeira ocorrência da palavra buscada. Caso não encontre, retorna -1.
print(encontrou)

encontrou = nova_frase.lower().find('presunto')
print(encontrou)

# Interpolação de variáveis
# 3 formas de fazer: usando %, usando o método format e usando f strings 

nome = 'Laura'
idade = 21
saldo = 130.32342

# Old Style - %
print("Nome: %s | Idade: %d | Saldo: %.2f" % (nome, idade, saldo))
frase = "Olá me chamo %s e tenho %d anos" % (nome, idade)

# format
print("Nome: {} | Idade: {} | Saldo: {:.2f}".format(nome, idade, saldo))

print("Nome: {2} | Idade: {0} | Saldo: {1}".format(idade, saldo, nome))
print("Nome: {2} | Idade: {0} | Saldo: {1} | Nome: {2}".format(idade, saldo, nome))

print("Nome: {name} | Idade: {age} | Saldo: {balance}".format(name=nome, age=idade, balance=saldo))

dados = {"nome": "Laura", "idade": 19, "saldo": 123.12312}
dados = {"name": nome, "age": idade, "balance": saldo}
print("Nome: {name} | Idade: {age} | Saldo: {balance:.2f}".format(**dados))

# #f-string
frase = f"Olá me chamo {nome} e tenho {idade} anos"
print(f"Nome: {nome} | Idade: {idade} | Saldo: {saldo:7.2f}")

# Strings de múltiplas linhas
nome = "Laura"

mensagem= f"""
    Olá meu nome é {nome},
        Eu estou aprendendo Python.
Essa mensagem possui diferentes recuos.
"""

print(mensagem)

print("""
    ************MENU************

    1 - Depositar
    2 - Sacar
    3 - Sair
""")