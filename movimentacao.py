class Movimento:
    def __init__(self, side, valor, desc, payment, data) -> None:
        self.side = side
        self.valor = valor
        self.desc = desc
        self.payment = payment
        self.data = data
        return None
    
    def show(self):
        return {
            "side": self.side,
            "valor": self.valor,
            "desc": self.desc,
            'payment': {
                    'banco': self.payment.banco,
                    'limite': self.payment.limite,
                    'nome': self.payment.nome
                },
            "data": self.data
        }
