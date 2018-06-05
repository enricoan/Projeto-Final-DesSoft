# -*- coding: utf-8 -*-
"""
Created on Sat May 12 12:04:42 2018

@author: Jadson
"""
class Cliente: #Aqui definimos uma classe chamada posicao
    def __init__(self):
        self.carteira={} 
        self.saldo=1E4
        self.lucro=0
        self.posicao=0 #momento do jogo associado 
        
        #carteira é o dicionário estruturado em {acao:quantidade}, ex: {Tesla:400}
        #Ou seja, temos 400 ações da Tesla
        
    def compra (self, acao, preco, quantidade): #O metodo compra recebe de acao, quantidade e preco
        self.saldo-=quantidade*preco #Uma quantidade do nosso dinheiro é removida
        if acao in self.carteira: #testamos se a acao já existe no dicionario
            self.carteira[acao]+=quantidade
        else: #se ela n existir colocamos ela lá
            self.carteira[acao]=quantidade
    def venda(self, acao, preco, quantidade):
        self.saldo+=quantidade*preco
        if acao in self.carteira: #testamos se a acao já existe no dicionario
            self.carteira[acao]-=quantidade
        else: 
            self.posicao[acao]=quantidade

    def alinha_preco(self, posicao): #O metodo recebe a posicao em que o valor atual da acao está na lista e retorna um dicionário
            carteira=self.carteira
            carteira_lucro={}
            for empresa in carteira:
                quantidade=carteira.get(empresa)
                carteira_lucro[empresa]={}
                tempo,cotacao = f.geradordeserie(empresa)
                carteira_lucro[empresa]['quantidade']=quantidade
                carteira_lucro[empresa]['cotacao']=cotacao[posicao]
            return carteira_lucro
  

class Graficos:
    def __init__(self):
        self.tempo=[]
        self.valores_acoes=[]
