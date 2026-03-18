class Arista:
    def __init__(self, inicio, objetivo, id):
        self.id = id
        self.n0 = inicio
        self.n1 = objetivo

    def __str__(self):
        return f'{self.n0}--{self.n1}'


    