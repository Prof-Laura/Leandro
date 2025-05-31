# Estruturas condicionais 
# if, elif e else 

idade = int(input('Digite a sua idade: '))

if idade < 18:
    print('Você é considerado uma criança/adolescente!')
elif 60 > idade >= 18:
    print('Você é considerado um adulto!')
else:
     print('Você é considerado um idoso!')

nome = 'Leandro'

if nome == 'Leandro':
    print('Você é aluno da Laura!')
else:
    print('Você não é um aluno da Laura')

# if ternário - é um if de uma linha

nota = 7.0

if nota >= 6.0:
    print('Aprovado')
else:
    print('Reprovado')

resultado = 'Aprovado' if nota>= 6.0 else 'Reprovado'
print(resultado)    

# Estruturas de repetição
# while e for

linguagem = 'Python'

for letra in linguagem:
    print(letra)

numero = 0

while numero < 10:
    print(numero)
    numero += 1
else:
    print('Fim do laço while')

# função range() - valor inicial, valor final da sequência (exclusivo) e passo/pulo (opcional)
for numero in range(0, 6):
    print(numero, end = ' ')

print()

for numero in range(2, 11, 2):
    print(numero, end=' ')

nome = 'Laura'

# # len - length - tamanho
# # Se você passsar apenas um número no range, o Python entende que você está passando o valor final. O valor incial começa com 0 automaticamente.
for num_letra in range(len(nome)):
    print(f'Letra na posição {num_letra}: {nome[num_letra]}')

# Estruturas de repetição com condicionais
lista_num_par = []

# Colocar na lista números pares
for numero in range(1, 101):
    if numero % 2 == 0:
        lista_num_par.append(numero) # adicionar o número na lista
    
for numero in lista_num_par:
    print(numero, end= ' ')

    continue
for num in range(5):
    if num == 3:
        print('Encontrei o 3')
        continue
    else:
        print(num)

    print('Estou abaixo do IF')

# break

numero = int(input('Digite um número entre 0 e 10: '))

for num in range(11):
    print(num, end= ' ')
    if numero == num:
        break
else:
    print()
    print('Número não encontrado!')

# pass
for item in range(5001):
    pass