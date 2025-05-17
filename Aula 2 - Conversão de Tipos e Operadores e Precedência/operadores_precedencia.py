## Operadores Aritméticos

# Soma
valor = 12 + 4
print(valor)

# Subtração
valor = 12 - 4
print(valor)

# Multiplicação
valor = 12 * 4
print(valor)

# Divisão
valor = 12 / 4
print(valor)

# Divisão que gera inteiro
valor = 12 // 4
print(valor)

# Exponenciação
valor = 3 ** 3
print(valor)

# Módulo
valor = 12 % 3
print(valor)

valor = 12 % 10
print(valor)

## Precedência
# 1° - Parênteses
# 2° - Exponenciações
# 3° - Multiplicações e Divisões
# 4° - Somas e subtrações

## Atribuições
saldo = 0
saldo += 200 # saldo = saldo + 200
saldo -= 100 # saldo = saldo - 100
saldo *= 2 # saldo = saldo * 2
saldo /= 2 # saldo = saldo / 2
saldo //= 2 # saldo = saldo // 2
saldo **= 2 # saldo = saldo ** 2
saldo %= 10 # saldo = saldo % 10

## Operadores de comparação
# = < > !

valor1 = 4
valor2 = 10

# print(valor1 > valor2)
# print(valor1 < valor2)
# print(valor1 >= valor2)
# print(valor1 <= valor2)
# print(valor1 == valor2)
# print(valor1 != valor2) # diferente

## Operadores lógicos
# and	Retorna True se ambas as afirmações forem verdadeiras
# or	Retorna True se uma das afirmações for verdadeira
# not	retorna Falso se o resultado for verdadeiro

# print(valor1 == 3 and valor2 == 10)
# print(valor1 <= 4 or valor2 > 10)

valor1 = True
# print(valor1)
# print(not valor1)
# print(not not valor1)

## Operadores de identidade
# is	Retorna True se ambas as variáveis são o mesmo objeto
# is not	Retorna True se ambas as variáveis não forem o mesmo objeto

limite, saldo = 200, 200
print(limite is saldo)

curso = "Curso de Python"
nome_curso = "Python"

print(nome_curso is curso)
print(nome_curso is not curso)

## Operadores de associação
# in	Retorna True caso o valor seja encontrado na sequência
# not in	Retorna True caso o valor não seja encontrado na sequência
print("python" in curso)
print("Python" in curso)

frutas = ["laranja", "banana", "melancia"]
print("maçã" not in frutas)

saques = [1500, 200]
print(100 in saques)

# Mostrando que 'is' não é igual a '=='
x = 10.0
y = 10

print(x, y)

print(x is y) # retorna False
print(x == y)

# Use is para verificar a identidade do objeto
# Use == para verificar valores