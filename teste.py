from models.cliente import Cliente
from models.conta import Conta

natalina: Cliente = Cliente('Natalina', 'natalia@hotmail.com', '222.222.222-22', '08/08/1999')

print(natalina)

contaa: Conta = Conta(natalina)