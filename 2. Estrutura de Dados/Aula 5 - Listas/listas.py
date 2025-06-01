# Listas são estruturas de dados que armazenam de maneira sequencial qualquer tipo de objeto. 
# Listas são objetos mutáveis, portanto podemos alterar seus valores após a criação.

frutas = ["laranja", "maçã", "banana"]
frutas = []
print(frutas)

letras = list()
letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

print(carro[0])
carro[0] = "ferrari"
print(carro)

print(carro[-1])
print(carro[-4])

# Lista aninhada
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

# Fatiamento
letras = list("python")
print(letras[2:])
print(letras[:2])
print(letras[1:3])
print(letras[0:3:2])
print(letras[::])
print(letras[::-1])

# Percorrendo uma lista
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# enumerate
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# List comprehension - Compreensão de Listas
numeros = [1, 30, 21, 2, 9, 65, 43]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

pares = []
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)

quadradp = []
quadrado = [numero ** 2 for numero in numeros]
print(quadrado)

## Métodos da classe list

# [].append - adiciona um objeto ao final da lista
lista = []
lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])
print(lista)

# [].clear - esvazia a lista
lista.clear()
print(lista)

# [].copy - copia o conteúdo para outra lista
lista = [1, "Python", [40, 30, 20]]
lista2 = lista.copy()
print(lista, lista2)
print(id(lista), id(lista2))

lista2 = lista
lista2.append(1)
print(lista2, lista)
print(id(lista), id(lista2))

# [].extend - adiciona mais de um elemento em uma lista
linguagens = ["python", "js", "c"]
linguagens.extend(["java", "csharp"])
print(linguagens)

# [].index - para saber o índice de um objeto específico
print(linguagens.index("java"))
print(linguagens.index("python"))

# [].pop - retira o último elemento da lista se não passar o índice
linguagens.pop()
print(linguagens)
linguagens.pop()
print(linguagens)
linguagens.pop(0)
print(linguagens)

# [].remove - retira um objeto específico
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.remove("js")
print(linguagens)

# [].reverse - reverte a ordem dos elementos da lista
linguagens.reverse()
print(linguagens)

# [].sort - ordena por ordem alfabética ou crescente
linguagens = ["python", "js", "c", "java", "csharp"]
nova_lista = linguagens.copy()
nova_lista.sort()
print(nova_lista, linguagens)

nova_lista.sort(reverse=True)
print(nova_lista)

# O que significa key=lambda x: len(x)
# Isso é um critério personalizado de ordenação.
# 🔑 key= define uma função que será usada para determinar o valor usado na ordenação.
# lambda x: len(x) significa: "Para cada item x, use o comprimento dele (len(x)) como chave de comparação."
# 💡 Em outras palavras, você está dizendo: "Ordene pela quantidade de caracteres de cada item."

#ordena por tamanho das palavras, ordem crescente
#lambda é uma função anônima (não tem nome)
#x é o argumento
#len tira o tamanho da string, quantidade de caracteres

linguagens.sort(key = lambda variavel: len(variavel))
print(linguagens)

linguagens.sort(key=lambda objeto: len(objeto), reverse=True)
print(linguagens)

# len - tamanho da lista
print(len(linguagens))

# | **`sort()`**                              | **`sorted()`**                                                                |
# | ----------------------------------------- | ----------------------------------------------------------------------------- |
# | É um **método de listas**.                | É uma **função embutida** do Python.                                          |
# | **Modifica a lista original** (in-place). | **Cria uma nova lista ordenada**, não altera a original.                      |
# | Só funciona com listas.                   | Funciona com **qualquer iterável** (listas, tuplas, dicionários, sets, etc.). |
# | Sintaxe: `lista.sort()`                   | Sintaxe: `sorted(iterável)`                                                   |

# sorted - ordena iteráveis
print(sorted(linguagens, key=lambda x:len(x)))
print(sorted(linguagens, key=lambda objeto: len(objeto), reverse=True))
print(sorted(linguagens))
print(linguagens)