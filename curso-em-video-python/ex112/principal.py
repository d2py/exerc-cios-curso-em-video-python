
from ex112.utilidadescv import moeda
from ex112.utilidadescv import dado

pr = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(pr, 20, 18)
