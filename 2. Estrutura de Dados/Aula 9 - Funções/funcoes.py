# Funções
# Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros, esses parâmetros podem ou não ter valores padrões. Usar funções torna o código mais legível e possibilita o reaproveitamento de código. Programar baseado em funções, é o mesmo que dizer que estmaos programando de maneira estruturada.

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# exibir_mensagem()
# exibir_mensagem2("Laura")
# exibir_mensagem3()
# exibir_mensagem3(nome="Leandro")

# Retorno
# return = None

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

# print(calcular_total([10, 20, 34]))
# print(retorna_antecessor_e_sucessor(50))

# Chave=Valor
def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
# salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
# salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

# Args e kwargs
# args - tuplas - posicionais
# kwargs - dicionários - nomeados

def exibir_poema(data_extenso, *args, **kwargs):
    texto="\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

# exibir_poema("Zen of Python", "Beautiful is better than ugly.", "Explicit is better than implicit", "Sei lá", "Olá", autor="Tim Peters", ano=1999)

# Parâmetros especiais
# /, 8
# / -> tudo antes da / só pode ser passado por posição
# * -> tudo que estiver depois só pode ser passado por nomeação

def criar_carro(marca, modelo, ano, /, placa, motor, combustivel):
    print(marca, modelo, ano, placa, motor, combustivel)

# criar_carro("Fiat", "Palio", 1999, placa="ABC-1234", motor="1.0", combustivel="Gasolina")
# criar_carro(marca="Fiat", "Palio", 1999, placa="ABC-1234", motor="1.0", combustivel="Gasolina")

def criar_carro(marca, modelo, ano, *, placa, motor, combustivel):
    print(marca, modelo, ano, placa, motor, combustivel)

# criar_carro("Fiat", "Palio", 1999, placa="ABC-1234", motor="1.0", combustivel="Gasolina")

def criar_carro(marca, modelo, ano, /, *, placa, motor, combustivel):
    print(marca, modelo, ano, placa, motor, combustivel)

criar_carro("Fiat", "Palio", 1999, placa="ABC-1234", motor="1.0", combustivel="Gasolina")

# Objetos de primeira classe

# Atribuir a uma variável
# Passar como argumento para outra função
# Retornar de uma função (closures)
# Armazenar em estruturas de dados (listas, conjunots, tuplas....)

def somar(a, b):
    return a+b

def exibir_resultados(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação {a} + {b} = {resultado}')

exibir_resultados(10, 10, somar)