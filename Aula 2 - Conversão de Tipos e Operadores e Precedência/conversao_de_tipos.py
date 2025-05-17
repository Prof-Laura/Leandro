## Boas Práticas do Python

# Snake case - espaços são substituidos por underline
# Variáveis com nomes sugestivos e completos

## Conversão de inteiro para float
# Primeira forma

preco = 10
print(preco)

preco = float(10) # preco = float(preco)
print(preco)

# Segunda forma

preco = 10 / 1 # Python transforma em float qualquer divisão
print(preco)

## Conversão de float para inteiro
preco = 10.0
preco = int(preco)
print(preco)

preco = 10.99
preco = int(preco)
print(preco)

## Divisão sem gerar número float
preco = 10 // 2
print(preco)

## Conversão de string para numérico
preco = "10.4"
idade = "21"

print(float(preco), int(idade))
# print(int(preco)) - gera erro, pois não consegue converter para inteiro a string que tem casa decimal

## Concatenando uma string com a variável
texto = f"Idade {idade} Preço {preco}"
print(texto)