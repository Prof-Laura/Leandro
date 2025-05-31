# print mostra um valor de qualquer tipo no terminal
print("Hello World") # str() - string

print(1 + 20 + 213) # int() - inteiro
print(1.4 + 34 + 1.2) # float() - ponto flutuante (números decimais)
print(True) # == 1  # bool() - variável booleana (Verdadeiro ou Falso)
print(False) # == 0 # bool()

# Se True realmente é igual/correspondente ('==') a 1 mostra no terminal a mensagem dentro do print
if True == 1:
    print('True corresponde a 1')

# Se False realmente é igual a 0 mostra no terminal a mensagem dentro do print
if False == 0:
    print('False corresponde a 0')

# Apenas um sinal de '=' significa atribuição
idade = 21
nome = "Laura"

# type() é uma função built-in (própria do python) que nos permite verificar o tipo da variável
print(type(idade))
print(type(nome))

# Como mostrar no terminal valores armazenados em uma variável juntamente com uma string
print(f'Meu nome é {nome} e eu tenho {idade} anos')

# Python consegue atribuir valores para variáveis de diferentes tipos em uma mesma linha
idade, nome, altura = 25, "Guilherme", 1.80
print(idade, nome, altura)

# end é o termino, que por padrão, é uma quebra de linha ('\n)
print(nome, idade, altura, end = '...\n')

# sep é o separador dessas variáveis, que por padrão, é um espaço
print(nome, idade, altura, sep = ' - ')

# input recebe dados do teclado, mas todos os dados são lidos como strings se não for especificado o tipo
sobrenome = input('Informe o seu sobrenome: ')
altura = float(input('Informe a sua altura: '))
nome = "Laura"
idade =  21

print(type(sobrenome))
print(type(altura))

# Concatenação de strings
print(f'O meu nome é {nome + " " + sobrenome}, eu tenho {idade} anos', end = '/')
print('Nome: ' + nome + ' Sobrenome: ' + sobrenome)

# Gera erro pois não é possível concatenar uma string com outros tipos de dados que também não sejam strings
# print('Nome: ' + nome + 'Idade: ' + idade)