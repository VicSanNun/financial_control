class Credito:
    def __init__(self, banco, limite, nome) -> None:
        self.banco = banco
        self.limite = limite
        self.nome = nome
        pass

    def update_limite(self, movimentacao):
        self.limite = self.limite - movimentacao

    def show(self):
        return {
            "banco": self.banco,
            "nome":self.nome,
            "limite":self.limite
        }
    
    #para garantir que estou passando o valor do objeto e n a referencia
    def copy(self):
        return Credito(self.banco, self.limite, self.nome)

    def __repr__(self):
        return f"{self.nome} (Banco: {self.banco}, Limite: {self.limite})"