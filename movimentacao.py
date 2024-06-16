from payments.Credito import Credito
from datetime import datetime

class Movimento:
    def __init__(self, side:str, valor:float, desc:str, payment:any, data:datetime) -> None:
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
