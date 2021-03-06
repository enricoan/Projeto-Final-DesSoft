# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:13:54 2018

@author: Enrico Aloisi Nardi
"""
from firebase import firebase
import tkinter as tk
import tkinter.ttk as ttk

def geradordeserie(nome_arquivo): #O nome precisa ser uma string
    #Abrindo arquivo e lendo os dados
    with open('txts/' + nome_arquivo +'.txt','r') as empresa:
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

def buy(cliente, acao, preco, linkedValue, quantidade=100): #nome do cliente(string), acao(string), quantidade(int)(variavel opcional), e preco(float)
    cliente.compra(acao, preco, quantidade)
    linkedValue.set(cliente.saldo)

#Função para venda de açõeslinkedValue

def sell(cliente,acao , preco,linkedValue, quantidade=100):
    cliente.venda(acao, preco, quantidade)
    linkedValue.set(cliente.saldo)

def retrieve_game(instancia): #pega os dados disponiveis na nuvem e atribui ao objeto da classe 'Clientes'
        firebase1=firebase.FirebaseApplication('https://projeto-final-dessoft.firebaseio.com/carteiras/cliente/', None)
        carteira_online=firebase1.get('carteira',None)
        saldo_online=firebase1.get('saldo',None)
        instancia.carteira=carteira_online
        instancia.saldo=saldo_online
    
def save_game(instancia): #instancia é o objeto da classe Clientes, modo é fácil, medio ou dificil
        firebase3=firebase.FirebaseApplication('https://projeto-final-dessoft.firebaseio.com/carteiras/cliente/', None)   
        cliente={'cliente':{'carteira':instancia.carteira, 'saldo':instancia.saldo}}
        firebase3.patch('https://projeto-final-dessoft.firebaseio.com/carteiras', cliente )


#função que calcula o lucro
def lucro(cliente, posicao, saldo_inicial= 1E5):
        carteira_lucro= cliente.alinha_preco(posicao)
        total=cliente.saldo
        for empresa in carteira_lucro:
            quantidade=carteira_lucro[empresa]['quantidade']
            cotacao=carteira_lucro[empresa]['cotacao']
            total+=quantidade*cotacao
        cliente.lucro = 100*(total-saldo_inicial)/saldo_inicial #lucro percentual


#Função que nos ajuda a mostrar o portifolio
def mostracarteira(instancia):
    carteira=''
    for k,v in instancia.carteira.items():
        carteira+='{0} | {1} \n'.format(k, v)
    return carteira


def mostralucro(instancia, posicao):
    lucro(instancia,posicao)
    return instancia.lucro
    
#Função que chama um pop-up de alerta para o usuário
    
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)


def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Atenção!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Ok", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def popupdeconfirmacao(modo, instancia):
    if modo=='salvamento':
        save_game(instancia)
        popupmsg('Jogo salvo com sucesso!')   
    elif modo=='carregamento':
        retrieve_game(instancia)
        popupmsg('Jogo carregado com sucesso!')
def popupsalvamento(instancia):
    popup = tk.Tk()
    popup.wm_title("Salvar o jogo")
    msg='Tem certeza que deseja salvar o jogo?'
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Sim", command = lambda: popupdeconfirmacao('salvamento', instancia) and popup.destroy)
    B1.pack()
    B2 = ttk.Button(popup, text="Não", command = popup.destroy)
    B2.pack()
    popup.mainloop()
    
def popucarregamento(instancia):
    popup = tk.Tk()
    popup.wm_title("Recuperar carteira salva")
    msg='Tem certeza que deseja carregar jogo anteriormente salvo?'
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Sim", command = lambda: popupdeconfirmacao('carregamento', instancia) and popup.destroy)
    B1.pack()
    B2 = ttk.Button(popup, text="Não", command = popup.destroy)
    B2.pack()
    popup.mainloop()
 
