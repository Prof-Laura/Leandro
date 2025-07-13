### Herança Simples ###

# Classe pai/base
class Veiculo:
    def __init__(self, placa, cor, num_rodas):
        self.placa = placa
        self.cor = cor
        self.num_rodas = num_rodas

    # Métodos
    def ligar_motor(self):
        print("Ligando o motor...")

    def status(self):
        return f'Cor: {self.cor} - Placa: {self.placa} - N° Rodas: {self.num_rodas}'
    
# Começa a herança simples
# Sem sobrescrever
class Moto(Veiculo):
    pass

# Sobrescrevendo
class Caminhao(Veiculo):
    def __init__(self, placa, cor, num_rodas, carregado):
        super().__init__(placa, cor, num_rodas)
        self.carregado = carregado

    # Sem o super
    """
    def __init__(self, placa, cor, num_rodas, carregado):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas
        self.carregado = carregado
    """

    # Método
    def esta_carregado(self):
        print(f'{"Sim," if self.carregado else "Não"} estou carregado')

        """
        if self.carregado == True:
            print("Sim, estou carregdo")
        else:
            print("Não estou carregado")    
        """

### Instanciar novos objetos
# Instanciando moto / classe sem sobrescer
print("-"*5 + "Usando a classe moto" + "-"*5)
motocicleta = Moto("ABC-123", "Preta", 2)
print(motocicleta.status())
motocicleta.ligar_motor()
print()

# Instanciando caminhao / classe sobrescrita
print("-"*5 + "Usando a classe caminhao" + "-"*5)
caminhao = Caminhao("ABC-456", "Branco", 8, True)
print(caminhao.status())
caminhao.ligar_motor()
caminhao.esta_carregado()