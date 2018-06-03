#importar bibliotecas
import scipy.stats
import numpy as np
import random
import os

#PATH das empresas
path = 'C:/Users/DiamonD/PycharmProjects/ep/Bolsas Tecnologia'
diretorio = os.listdir(path)

"""Números da Sorte[0]"""

sorte_alta = []
sorte_media = []
sorte_baixa = []

#Gerar numeros da sorte para cada empresa
for e in range(len(diretorio)):
    tendencia = 0.5  # numero mais provavel de cair
    aleatorio = abs(scipy.stats.norm.rvs(loc=0, scale=tendencia))  # valor absoluto do numero sorteado
    if aleatorio < tendencia / 5:
        sorte_alta.append(aleatorio)
    elif aleatorio > tendencia / 1.5:
        sorte_media.append(aleatorio)
    else:
        sorte_baixa.append(aleatorio)

"""FIM Números da Sorte[0]"""


""""Gerador de graficos [1]"""

def gerador_acoes(multiplicador_sorte, somador_sorte, divisor_sorte):
    time = np.arange(0, 20, 20/1259)
    graph = []
    acao = []

    # Amplitude do valor das ações
    amplitude = (np.cos(time) * multiplicador_sorte + somador_sorte) / divisor_sorte

    # Adicionar variação a amplitude
    for e in amplitude:
        rvs = scipy.stats.norm.rvs(loc=0, scale=2)
        graph.append(e + rvs)
    #Adicionar a variavel acao no formato de lista: Tempo Valor_Ação
    for e in range(len(time)):
        acao.append('{0} {1}'.format(e, graph[e]))

    # Formatacao para adicionar aos arquivos
    acao_string = '\n'.join(acao)

    #Retornar acao formatada
    return acao_string

""""FIM Gerador de graficos [1]"""


""""Gerador txt [2]"""

for e in range(len(sorte_alta)):
    multiplicador_sorte = random.randint(40, 60)
    somador_sorte = random.randint(240, 600)
    divisor_sorte = random.randint(3, 4)
    gerador = gerador_acoes(multiplicador_sorte, somador_sorte, divisor_sorte)

    with open('{0}/{1}'.format(path, diretorio[e]), 'w') as saida:
        saida.write(gerador)

for e in range(len(sorte_alta), len(sorte_alta)+len(sorte_media)):
    multiplicador_sorte = random.randint(60, 70)
    somador_sorte = random.randint(240, 326)
    divisor_sorte = random.randint(4, 6)
    gerador = gerador_acoes(multiplicador_sorte, somador_sorte, divisor_sorte)

    with open('{0}/{1}'.format(path, diretorio[e]), 'w') as saida:
        saida.write(gerador)
for e in range(len(sorte_alta)+len(sorte_media), len(sorte_alta)+len(sorte_media)+len(sorte_baixa)):
    multiplicador_sorte = random.randint(20, 40)
    somador_sorte = random.randint(100, 254)
    divisor_sorte = 6
    gerador = gerador_acoes(multiplicador_sorte, somador_sorte, divisor_sorte)

    with open('{0}/{1}'.format(path, diretorio[e]), 'w') as saida:
        saida.write(gerador)
""""FIM Gerador txt [2]"""