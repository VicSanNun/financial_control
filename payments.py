class Payments():
    def __init__(self) -> None:
        pass

    def credito(self, banco, nome):
        return {
            "banco": banco,
            "nome":nome
        }
    
    def debito(self, banco, nome):
        return {
            "banco": banco,
            "nome":nome
        }
    
    def pix(self, banco, nome):
        return {
            "banco": banco,
            "nome":nome
        }