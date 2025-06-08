### Tuplas
## Criação
tupla1 = ()
tupla2 = tuple()

print(type(tupla1), type(tupla2))

nome = ("laura")
print(type(nome))

nome = ("leandro",)
print(type(nome))

nomes = ("laura", "leandro")
print(type(nomes))

tupla = ([1, 2, 3, 4],)

## Acesso direto
frutas = ("maçã", "banana", "pera", "melancia")
print(frutas[0])
print(frutas[2])
print(frutas[-1])
print(frutas[-3])

# Erro ao tentar alterar por índice

# frutas[0] = "uva"

## Tuplas aninhadas
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

## Fatiamento
tupla = ("p", "y", "t", "h", "o", "n")

print(tupla[2:]) # ("t", "h", "o", "n")
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1])

## Iterar tuplas
carros = ("gol", "celta", "palio")
for carro in carros:
    print(carro)

# Funçãpo enumerates
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

## Métodos da classe tuple

# count
cores = ("vermelho", "azul", "verde", "azul")

print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

# index
linguagens = ("java", "csharp", "python", "html")
print(linguagens.index("java"))
print(linguagens.index("python"))

# len
print(len(linguagens))

# sorted
print(sorted(linguagens)) 

# Curiosidades
coordenadas = (-23.588254, -46.632477)
print(id(coordenadas))
coordenadas += (-5,)
print(coordenadas)
print(id(coordenadas))

tupla = ([1, 2, 3],['a', 'b', 'c'])
print(id(tupla))
tupla[0].append(4)
print(tupla)
print(id(tupla))