'''
Criar uma class Carro com dois atributos compostos por duas outras classes:
1. Motor
2. Direção

A classe Motor deve controlar a velocidade, ele oferece os seguintes atributos:
1. Atributo de dado velocidade
2. Método acelerar, que deverá incrementar print(o valor) de uma unidade 
3. Método desacelerar, que deverá decrementar a velocidade em duas unidades

A Direção oferece os seguintes atributos:
1. Direção com os valores possíveis: 
    a. Norte
    b. Sul
    c. Leste
    d. Oeste
2. Método girar a direita
3. Método girar a esquerda

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.desacelerar()
    >>> motor.velocidade
    1
    >>> motor.desacelerar()
    >>> motor.velocidade
    0
    >>> # Testando direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.virar_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.virar_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.virar_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.virar_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.virar_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.virar_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.virar_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.virar_esquerda()
    >>> direcao.valor
    'Norte'
    >>> # Testando carro
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.desacelerar()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.virar_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.virar_direita()
    >>> carro.calcular_direcao()
    'Norte'
'''


class Motor():
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def desacelerar(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao():
    rotacao_direita = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_esquerda = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }
    
    def __init__(self):
        self.valor = NORTE
        
    def virar_esquerda(self):
        self.valor = self.rotacao_esquerda[self.valor]

    def virar_direita(self):
        self.valor = self.rotacao_direita[self.valor]

class Carro:
    def __init__(self, direcao=None, motor=None):
        self.direcao = direcao
        self.motor = motor
    
    def calcular_direcao(self):
        return self.direcao.valor

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()
    
    def desacelerar(self):
        self.motor.desacelerar()
    
    def virar_esquerda(self):
        self.direcao.virar_esquerda()
    
    def virar_direita(self):
        self.direcao.virar_direita()


