from caixa import Caixa
from movimentacao import Movimento
from payments.Credito import Credito
from datetime import datetime
from pprint import pprint

caixa = Caixa()
nubank = Credito("Nubank", 2000, "Credito Nubank")
inter = Credito("Inter", 700, "Credito Inter")


salario = Movimento("E", 3000, "Salário", "Dinheiro", datetime.today())

ifood = Movimento("S", 100, "IFood", inter.copy(), datetime.today())
inter.update_limite(ifood.valor)

gasolina = Movimento("S", 50, "gasoline", nubank.copy(), datetime.today())
nubank.update_limite(gasolina.valor)

sorvete = Movimento("S", 20, "sorvete", nubank.copy(), datetime.today())
nubank.update_limite(sorvete.valor)

#caixa.append(salario)
caixa.append(ifood)
caixa.append(gasolina)
caixa.append(sorvete)

pprint(caixa.show())
