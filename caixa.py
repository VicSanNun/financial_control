class Caixa:
    def __init__(self) -> None:
        self.caixa = []
        return None
    
    def append(self, movimento):
        self.caixa.append(movimento)
        return None
    
    def show(self):
        return [movimento.show() for movimento in self.caixa]
