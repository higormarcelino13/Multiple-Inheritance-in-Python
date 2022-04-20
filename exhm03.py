#Implemente as classes de modo que obedeçam os relacionamentos apresentados no diagrama abaixo.
#O método acelerar deve somar o valor passado por parâmetro à velocidade do veículo.
#O método frear  deve subtrair o valor passado por parâmetro da velocidade do veículo.
#Os métodos imprimir_informacoes das classes Carro, Moto e Bicicleta deve exibir na tela o valor de cada um dos atributos da classe (inclusive os atributos herdados da superclasse)

class Veiculo:
    def __init__(self, marca, modelo, rodas):
        self.marca = marca
        self.modelo = modelo
        self.rodas = rodas
        self.velocidade = 0
        
    def acelerar(self, valor):
        self.velocidade += valor
        
    def frear(self, valor):
        self.velocidade -= valor
        
    def get_velocidade(self):
        return self.velocidade
    

class Automovel(Veiculo):
    def __init__(self, marca, modelo, rodas, potencia):
        super().__init__(marca, modelo, rodas)
        self.potencia = potencia
    
    def imprimir_informacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Rodas: {self.rodas}')
        print(f'Potência: {self.potencia}')
        print(f'Velocidade: {self.get_velocidade()}')
        
class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, rodas, marcha, bagageiro):
        super().__init__(marca, modelo, rodas)
        self.marcha = marcha
        
    def imprimir_informacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Rodas: {self.rodas}')
        print(f'Marcha: {self.marcha}')
        print(f'Velocidade: {self.get_velocidade()}')
        
        
class Carro(Automovel):
    def __init__(self, marca, modelo, rodas, potencia, portas):
        super().__init__(marca, modelo, rodas, potencia)
        self.portas = portas
    
    def imprimir_informacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Rodas: {self.rodas}')
        print(f'Potência: {self.potencia}')
        print(f'Portas: {self.portas}')
        print(f'Velocidade: {self.get_velocidade()}')
        
        
class Moto(Automovel):
    def __init__(self, marca, modelo, rodas, potencia, partida_eletrica):
        super().__init__(marca, modelo, rodas, potencia)
        self.partida_eletrica = partida_eletrica
        
    def imprimir_informacoes(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Rodas: {self.rodas}')
        print(f'Potência: {self.potencia}')
        print(f'Partida Elétrica: {self.partida_eletrica}')
        print(f'Velocidade: {self.get_velocidade()}')


carro = Carro("Ford", "Ka", 4, 85.0, 5)
moto = Moto("Honda", "Biz", 2, 9.2, True)
bike = Bicicleta("Caloi", "Elite", 2, 18, True)
 
carro.acelerar(30)
carro.frear(10)
moto.acelerar(100)
moto.frear(20)
bike.acelerar(20)
bike.frear(5)
 
carro.imprimir_informacoes()   # imprime os valores de todos os atributos do carro
bike.imprimir_informacoes()    # imprime os valores de todos os atributos da bicicleta
moto.imprimir_informacoes()    # imprime os valores de todos os atributos da moto
 
# testar a velocidade atual
print("Velocidade atual do Carro:", carro.get_velocidade())       # 20
print("Velocidade atual da Moto:", moto.get_velocidade())         # 80
print("Velocidade atual da Bicicleta:", bike.get_velocidade())    # 15