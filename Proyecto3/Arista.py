class Arista:
    def __init__(self, inicio, objetivo, id, weight):
        self.id = id
        self.n0 = inicio
        self.n1 = objetivo
        self.weight = weight

    def __str__(self):
        return f'{self.n0}--{self.n1}'

    def get_nodo0(self):
        return self.n0
    
    def get_nodo1(self):
        return self.n1

    def get_weight(self):
        return self.weight
    