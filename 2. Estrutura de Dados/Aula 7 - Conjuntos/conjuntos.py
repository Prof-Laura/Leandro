### Conjuntos/Set

## Criação
conjunto = {1, "Laura", 1.32}
print(conjunto)

conjunto = set("Laura")
print(conjunto)

print(set([1, 2, 3, 1, 3, 4]))
print(set(("palio", "gol", "celta", "palio")))

linguagens = {"python", "java", "python"}
print(linguagens)

## Conversão
numeros = {1, 2, 3, 4}
numeros = list(numeros)
print(numeros[0])

## Iteração
carros = {"palio", "celta", "uno", "gol"}

for carro in carros:
    print(carro)

# Função enumerate
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

## Métodos

# union
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4}
print(conjunto_a.union(conjunto_b))

# intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
print(conjunto_a.intersection(conjunto_b))

# difference
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# symetric_difference
print(conjunto_a.symmetric_difference(conjunto_b)) # todos elementos diferentes entre A e B

# issubset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

# issuperset
print(conjunto_a.issuperset(conjunto_b))
print(conjunto_b.issuperset(conjunto_a))

# isdisjoint
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

# add

numeros = {1, 23}
numeros.add(25)
numeros.add(42)
numeros.add(25)

print(numeros)

# clear

numeros.clear()
print(numeros)

# copy
numeros = {1, 23}
numeros.copy()
print(numeros)

# discard 
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)
print(numeros)

# remove
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.remove(1)
# numeros.remove(45) - retorna um erro
print(numeros)

# pop
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
print(numeros.pop())
print(numeros.pop())
print(numeros)

nomes = {"laura", "leandro", "guilherme", "ana"}
print(nomes.pop())
print(nomes.pop())
print(nomes)

# len
print(len(numeros))

# in
print(1 in numeros)
print(45 in numeros)