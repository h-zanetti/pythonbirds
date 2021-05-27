class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome='Jesus Cristo', idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimento(self):
        return f"Olá, {self.nome}!"

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def metodo_de_classe(cls):
        return f"{cls} tem {cls.olhos} olhos"

if __name__ == '__main__':
    h = Pessoa(nome='Henrique', idade=21)
    p = Pessoa(h)
    print(f"{Pessoa.cumprimento(p)}\n{h.cumprimento()}\n")
    p.olhos = 1
    print(f"{p.nome} tem {p.olhos} olho\n{h.nome} tem {h.olhos} olhos\n")
    print(f"{p.nome} tem {len(p.filhos)} filho\n{h.nome} tem {len(h.filhos)} filhos\n")
    