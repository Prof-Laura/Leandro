# Constantes em Python na realidade não existem de fato, pois tudo é entendido como objeto
# O que a comunidade fez foi a criação de uma convenção, onde toda constante seria então uma variável com o nome totalmente em maiúsculo.

# Por convenção esses números são entendidos como constante por nós, mas não para o python.
PI = 3.14159
NUMERO_EULER = 2.71828
print(PI, NUMERO_EULER)

# Como é apenas uma convenção, é possível mudar o valor que essas variáveis armazenam, mas NÃO É O IDEAL
PI = 1.7
print(PI)