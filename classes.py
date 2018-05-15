# -*- coding: utf-8 -*-
"""
Created on Sat May 12 12:04:42 2018

@author: Jadson
"""
class Clientes: #Aqui definimos uma classe chamada posicao
    def __init__(self):
        self.carteira={} 
        self.saldo=1E4
        #Essa classe possui dois atributos: posição, um dicionário e dinheiro, um inteiro
        #posicao é o dicionário estruturado em {acao:quantidade}, ex: {Tesla:400}
        #Ou seja, temos 400 ações da Tesla
        #Dinheiro é o saldo disponível no banco para compra de ações
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