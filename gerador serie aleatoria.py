#importar bibliotecas
import scipy.stats
import numpy as np
import random
import os

#PATH das empresas
path = 'C:/Users/DiamonD/PycharmProjects/ep/Bolsas Bem de Consumo'
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

def gerador_acoes(valor_inicial, soma_escala, escala_inicial):
    time = np.arange(0, 20, 20/1259)
    graph = []
    acao = []

    # Amplitude do valor das ações
    amplitude = np.cos(time) + valor_inicial
    scale = escala_inicial

    # Adicionar variação a amplitude
    for i in range(1259):
        graph.append(abs(amplitude[i] + scipy.stats.norm.rvs(loc=0, scale=scale)))
        scale += soma_escala
    # Adicionar a variavel acao no formato de lista: Tempo Valor_Ação
    for e in range(len(time)):
        acao.append('{0}, {1}'.format(e, graph[e]))

    # Formatacao para adicionar aos arquivos
    acao_string = '\n'.join(acao)

    #Retornar acao formatada
    return acao_string
# acao = np.cos(t) + 80
# scale=0.3
# graph = []
# for i in range(1259):
#     graph.append(abs(acao[i] + scipy.stats.norm.rvs(loc=0, scale=scale)))
#     scale += 0.01
""""FIM Gerador de graficos [1]"""


""""Gerador txt [2]"""
# 20 a 50 fraco
# 51 a 120 medio
# 121 a 160 bom
for e in range(len(sorte_alta)):
    #sorte alta
    valor_inicial = random.randint(121, 180)
    soma_escala = random.uniform(0.0009, 0.002)
    escala_inicial = random.uniform(0.9, 1)
    gerador = gerador_acoes(valor_inicial, soma_escala, escala_inicial)

    with open('{0}/{1}'.format(path, diretorio[e]), 'w') as saida:
        saida.write(gerador)

for e in range(len(sorte_alta), len(sorte_alta)+len(sorte_media)):
    #sorte media
    valor_inicial = random.randint(51, 120)
    soma_escala = random.uniform(0.001,0.006)
    escala_inicial = random.uniform(1.6, 2)
    gerador = gerador_acoes(valor_inicial, soma_escala, escala_inicial)

    with open('{0}/{1}'.format(path, diretorio[e]), 'w') as saida:
        saida.write(gerador)
for e in range(len(sorte_alta)+len(sorte_media), len(sorte_alta)+len(sorte_media)+len(sorte_baixa)):
    #sorte baixa
    valor_inicial = random.randint(20, 50)
    soma_escala = random.uniform(0.0008, 0.0001)
    escala_inicial = random.uniform(0.4, 1.6)
    gerador = gerador_acoes(valor_inicial, soma_escala, escala_inicial)

    with open('{0}/{1}'.format(path, diretorio[e]), 'w') as saida:
        saida.write(gerador)
""""FIM Gerador txt [2]"""
