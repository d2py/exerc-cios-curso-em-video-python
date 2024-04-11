'''pessoas = {'nome': 'Diego', 'idade': 32, 'sexo': 'M'}
pessoas['peso'] = 90.6
print(pessoas)
for k, v in pessoas.items():
    print(f'{k}= {v}')'''

#Dicionario dentro de uma lista
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''

'''estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for v in e.values():
        print(v, end=' ')'''



# Mostradondo a situação do aluno se e aprovado ou reprovado
aluno = dict()

aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))

if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'

elif aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
   aluno['Situação'] = 'Reprovado'
print('-='*35)
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
