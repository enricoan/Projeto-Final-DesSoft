#Função para gerar série temporal a partir de arquivo 
def geradordeserie(nome_arquivo): #O nome precisa ser uma string
    #Abrindo arquivo e lendo os dados
    with open(nome_arquivo +'.txt','r') as empresa:
        serie= empresa.read()
    
    #Spliting o arquivo nos pontos onde há quebra de linha
    linhas= serie.split('\n')
    
    #Lista tempo e lista cotação
    tempo=[]
    cotacao=[]
    #Percorre a lista linhas e adiciona os elementos em sua devida lista
    for linha in linhas:
       if len(linha)> 1:
            x,y = linha.split(',')
            tempo.append(float(x))
            cotacao.append(float(y))
    return tempo, cotacao

#Funções para compra e venda      
#Função para compra de ações

def buy(cliente, acao, preco, quantidade=100): #nome do cliente(string), acao(string), quantidade(int)(variavel opcional), e preco(float)
    cliente.compra(acao, preco, quantidade)

#Função para venda de ações

def sell(cliente, acao, preco, quantidade=100):
    cliente.venda(acao, preco, quantidade)

def lucro(cliente, posicao, saldo_inicial= 1E4):
        carteira_lucro= cliente.alinha_preco(posicao)
        total=cliente.saldo
        for empresa in carteira_lucro:
            quantidade=carteira_lucro[empresa]['quantidade']
            cotacao=carteira_lucro[empresa]['cotacao']
            total+=quantidade*cotacao
        cliente.lucro = 100*(total-saldo_inicial)/saldo_inicial #lucro percentual
