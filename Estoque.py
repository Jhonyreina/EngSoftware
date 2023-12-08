class Ingredientes:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"{self.nome} | preço: R$ {(self.preco):.2f} |  {self.quantidade} (g) ou (ml)"
        
    def get_preco(self):
        return float(self.preco)

    def to_csv(self):
        return [self.nome, float(self.quantidade), float(self.preco)]

    @classmethod
    def from_csv(cls, dados):
        return cls(dados[0], float(dados[1]), float(dados[2]))
