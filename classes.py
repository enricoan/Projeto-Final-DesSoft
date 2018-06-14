# -*- coding: utf-8 -*-
"""
Created on Mon May 14 12:13:20 2018

@author: Enrico Aloisi Nardi
"""
import funcoes as f

#Código para a mensagem pop-up

#Abaixo definimos uma classe chamada Clientes
#Cada objeto dessa classe será um cliente nosso
#Dois métodos são aplicáveis aos objetos dessas classe (cliente):
#Podemos comprar ou vender
class Cliente: 
    def __init__(self):
        self.carteira={} 
        self.saldo=1E5
        self.posicao=0
        #Essa classe possui dois atributos: carteira, um dicionário; e saldo, um float.
        #carteira é o dicionário estruturado em {acao:quantidade}, ex: {'Tesla':400}
        #Ou seja, temos 400 ações da Tesla
        #saldo é o dinheiro disponível no banco para compra de ações, nesse caso 10k 
        
    def compra (self, acao, preco, quantidade): #O metodo compra recebe de acao, quantidade e preco
        if self.saldo-quantidade*preco > 0: #testa se o resultado da compra deixa saldo positivo
            self.saldo -= quantidade*preco #Uma quantidade do nosso dinheiro é removida
            if acao in self.carteira: #testamos se a acao já existe no dicionario
                #testamos se ele tem saldo na carteira
                    self.carteira[acao] += quantidade # se ela existir só adicionamos a quantidade à ação
            else: #se ela n existir colocamos ela lá e lhe atribuimos o valor quantidade
                self.carteira[acao] = quantidade
        else:
            f.popupmsg('Saldo Insuficiente')
    def venda(self, acao, preco, quantidade):
        if self.carteira[acao]<quantidade:
            f.popupmsg('Você não possui ações suficientes para essa transação')
        else:
            self.saldo += quantidade*preco
            if acao in self.carteira: 
                self.carteira[acao] -= quantidade
            else: 
                self.carteira[acao] = quantidade
                
    def alinha_preco(self, posicao): #metodo que cria um dicionario com os valores da carteira no momento
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
