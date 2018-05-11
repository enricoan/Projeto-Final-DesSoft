import os

import os
path = 'C:/Users/DAMNROOT/Documents/Insper/1o semestre/Design de Software/Projeto Final/Bolsas'
for arquivo in os.listdir(path):

    with open ('{0}/{1}'.format(path, arquivo), 'r') as batata:
        linhas = batata.readlines()

    saida=[]
    for i in range(1, len(linhas)):
        linha = linhas[i]
        dados=linha.split(',')
        saida.append("{0},{1}".format(i-1,dados[5]))
    print('\n'.join(saida))
