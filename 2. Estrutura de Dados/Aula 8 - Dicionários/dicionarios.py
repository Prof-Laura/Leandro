### Dicionários
## {"chave": valor, "chave2": valor}

## Criação
pessoa = {"nome": "Laura", "idade": 21, "nome": "Leandro"}
print(pessoa)

pessoa = dict(nome = "Laura", idade = 21)
print(pessoa)

pessoa['sobrenome'] = "Oliveira"
print(pessoa)

print(pessoa['nome'])

pessoa['idade'] = 22
print(pessoa)

## Dicionário aninhado
dados = {
    "laura.s.oliveira2018@gmail.com": {"nome": "Laura", "sobrenome": "Oliveira", "idade": 21},
    "guilherme.oliveira@gmail.com": {"nome": "Guilherme", "sobrenome": "Oliveira", "idade": 25, "telefone": {"extra": "9999-9999"}}
}

print(dados["laura.s.oliveira2018@gmail.com"]["idade"])
print(dados["guilherme.oliveira@gmail.com"]["telefone"]["extra"])

## Iterar dicionários
for chave in dados:
    print(chave, dados[chave])

# melhor forma
for chave, valor in dados.items():
    print(chave, valor)

## Métodos

# clear
dados.clear()
print(dados)

# copy
dados = {
    "laura.s.oliveira2018@gmail.com": {"nome": "Laura", "sobrenome": "Oliveira", "idade": 21}
}

copia = dados.copy()
print(copia)

# fromkeys

resultado = dict.fromkeys(["nome", "telefone"])
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")
print(resultado)

# get
resultado = dados.get("chave")
print(resultado)

resultado = dados.get("chave", "Não foi encontrado")
print(resultado)

resultado = dados.get("laura.s.oliveira2018@gmail.com", "Não foi encontrado")
print(resultado)

# items 
print(dados.items())

# keys
print(dados.keys())

novo_dicionario = {"a": 100, "teste": "B", 1: "python"}
print(novo_dicionario.keys())

# pop
print(dados.pop("laura.s.oliveira2018@gmail.com"))
print(dados)
print(dados.pop("chave", "Chave não encontrada!"))

# popitem
dados = {
    "laura.s.oliveira2018@gmail.com": {"nome": "Laura", "sobrenome": "Oliveira", "idade": 21},
    "guilherme.oliveira@gmail.com": {"nome": "Guilherme", "sobrenome": "Oliveira", "idade": 25, "telefone": {"extra": "9999-9999"}}
}

print(dados.popitem())
print(dados)
print(dados.popitem())

# setdefault
dados = {
    "laura.s.oliveira2018@gmail.com": {"nome": "Laura", "sobrenome": "Oliveira", "idade": 21},
    "guilherme.oliveira@gmail.com": {"nome": "Guilherme", "sobrenome": "Oliveira", "idade": 25, "telefone": {"extra": "9999-9999"}}
}

dados["laura.s.oliveira2018@gmail.com"].setdefault("nome", "Geovanna")
print(dados["laura.s.oliveira2018@gmail.com"])

dados["laura.s.oliveira2018@gmail.com"].setdefault("telefone", "9999-9999")
print(dados)

# update
dados["laura.s.oliveira2018@gmail.com"].update({"nome": "Geovanna"})
print(dados["laura.s.oliveira2018@gmail.com"])

dados["laura.s.oliveira2018@gmail.com"].update({"Endereço": "Av. Sei la"})
print(dados["laura.s.oliveira2018@gmail.com"])

# values
print(dados.values())

# in 
print("laura.s.oliveira2018@gmail.com" in dados)
print("karla.s.oliveira2018@gmail.com" in dados)
print("nome" in dados["laura.s.oliveira2018@gmail.com"])
print("numero" in dados["laura.s.oliveira2018@gmail.com"])

# del 

del dados["laura.s.oliveira2018@gmail.com"]
del dados["guilherme.oliveira@gmail.com"]["telefone"]
print(dados)