# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:14:35 2018

@author: Enrico Aloisi Nardi
"""

""""BIBLIOTECA [*]"""
#bibliotecas matplotlib
from matplotlib import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
#from matplotlib import style
import matplotlib.pyplot as plt
#Bibliotecas tkinter
import tkinter as tk
import tkinter.ttk as ttk
from classes import Clientes
import funcoes as f
from firebase import firebase

#Criando o objeto 'cliente' e atribuindo-lhe dados disponíveis no firebase

firebase=firebase.FirebaseApplication('https://projeto-final-dessoft.firebaseio.com/', None)
carteiras= firebase.get('carteiras', None)
cliente=Clientes()
cliente.carteira=carteiras['cliente']['carteira']
cliente.saldo=carteiras['cliente']['saldo']

#importar o key_press_handler
#
from matplotlib.backend_bases import key_press_handler

""""FIM BIBLIOTECA [*]"""

""""FONTES PADRÃO E STYLE [0]"""
LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
style.use("ggplot")
""""FIM FONTES PADRÃO E STYLE [0]"""


""""FUNÇÕES UNIVERSAIS [1]"""
def popupmsg():
    popup = tk.Tk()
    popup.wm_title("!")
    label = tk.Label(popup, text= "batata", font = LARGE_FONT)
    label.pack(side="top", fill = "x", pady= 10)
    B1 = tk.Button(popup, text = "Okay", command = popup.destroy())
    B1.pack()
    popup.mainloop()

""""FIM DEFINIÇÃO FUNÇÕES UNIVERSAIS [1]"""


""""CONFIGURAÇÕES TKINTER [2]"""
class jogo(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Million Run")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MenuPage, Game, modo_facil, Dificulty):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(MenuPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
""""CONFIGURAÇÕES TKINTER [2]"""

""""MENU [3]"""
class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        bem_vindo= tk.Label(self, text= 'Seja bem-vindo ao Milion Run', font= LARGE_FONT)
        bem_vindo.place(x=0,y=0)
        
        button = tk.Button(self, text="Jogar!",command=lambda: controller.show_frame(Dificulty))
        button.pack()

        button3 = tk.Button(self, text="Visit Graph Page",command=lambda: controller.show_frame(modo_facil))
        button3.pack()        
""""FIM MENU [3]"""

"""DIFICULDADE [4]"""
class Dificulty(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label_dificuldade = tk.Label(self, text="Escolha a dificuldade", font=LARGE_FONT)
        label_dificuldade.place(x=0,y=0)
        
        button_dif1 = tk.Button(self, text="Fácil", font=NORMAL_FONT)
        button_dif1.place(x=0,y=30)
        
        button_dif2 = tk.Button(self, text="Normal",command=lambda:controller.show_frame(modo_facil), font=NORMAL_FONT)
        button_dif2.place(x=0,y=60)
        
        button_dif3 = tk.Button(self, text="Real", font=NORMAL_FONT, command=lambda:controller.show_frame(modo_difícil))
        button_dif3.place(x=0,y=90)
        
        button = tk.Button(self, text="Voltar para Home",command=lambda: controller.show_frame(MenuPage))
        button.place(x=0,y=120)
"""FIM DIFICULDADE [4]"""

""""JOGO [5]"""
class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        one = tk.Label(self, text="Million Run")
        one.place(x=1280 / 2, y=0)

        carteira = tk.Label(self, text="Carteira", font=LARGE_FONT)
        carteira.place(x=1100, y=100)
        
        botao_comprar = tk.Button(self, text="Vender", command= lambda: f.buy(cliente,'tesla',valores_acoes[i], quantidade= 100))
        botao_comprar.place(x=400, y=450)

        botao_vender = tk.Button(self, text="Comprar", command= lambda: f.sell(cliente,'tesla',valores_acoes[i], quantidade= 100))
        botao_vender.place(x=400, y=500)

        grafico = tk.Label(self, text="Grafico")
        grafico.place(x=200, y=475)

        total = tk.Label(self, text="Total: {0}".format(cliente.saldo), font=NORMAL_FONT)
        total.place(x=1100, y=650)
""""FIM JOGO [4]"""

""""PÁGINA GRÁFICO [6] // TESTE"""
lista_adicao= []
tempo_adicao= []
tempo = []
valores_acoes=[] 
i=0
class modo_facil(tk.Frame): #modo do jogo no qual eixos pessoa clica no botão e o valor da ação é plotado
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #labels da página
        titulo_pagina = tk.Label(self, text="CONTROLE DE PREÇOS", font=LARGE_FONT, underline=1)
        titulo_pagina.pack()
        
        mecanismo_busca= tk.Label(self, text= "Busque aqui a empresa desejada")
        mecanismo_busca.place(x=0,y=30)
        
        #botões da página
        voltar= tk.Button(self, text="Voltar",command=lambda: controller.show_frame(MenuPage))
        voltar.place(x=1000,y=0)
        
        plotador = tk.Button(self, text= 'Plotar mais um ponto', command= self.proximo_ponto)
        plotador.place(x=950,y=30)
        
        botao_comprar = tk.Button(self, text="Vender", command= lambda: f.buy(cliente,'tesla',valores_acoes[i], quantidade= 100))
        botao_comprar.place(x=500, y=70)

        botao_vender = tk.Button(self, text="Comprar", command= lambda: f.sell(cliente,'tesla',valores_acoes[i], quantidade= 100))
        botao_vender.place(x=550, y=70)
        
        #barra de pesquisa para as empresas
        cb= ttk.Combobox()
        cb.set('Busque aqui a empresa desejada')
        cb.place(x=0,y=0)
        
        #tudo o que precisamos para o gráfico atualizável
        fig = Figure(figsize=(2,2), dpi=100)
        self.eixos = fig.add_subplot(111)
        
        self.canvas = FigureCanvasTkAgg(fig, self)
        self.widget = self.canvas.get_tk_widget()
        self.eixos.set_autoscale_on(True)
        self.eixos.set_xlabel('Tempo (dias)')
        self.eixos.set_ylabel('Valor da ação (dólares)')
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
        self.canvas._tkcanvas.pack(side=tk.LEFT)
        
    #escolhendo a empresa (ainda precisa virar uma def para generalizar)

        with open('TSLA.txt','r') as arquivo:
            valorescsv = arquivo.read()
        linhas= valorescsv.split('\n')
        for linha in linhas:
            x,y= linha.split(',')
            tempo.append(int(x))
            valores_acoes.append(int(y))
    
    
    def proximo_ponto(self):
        global i
        self.eixos.set_title('TSLA')
        self.eixos.set_xlabel('Tempo (dias)')
        self.eixos.set_ylabel('Valor da ação (dólares)')
        lista_adicao.append(valores_acoes[i])
        tempo_adicao.append(tempo[i])
        
        valor_em_x = tempo[i]
        valor_em_y = valores_acoes[i]
        
        #por extenso e com diametro do ponto
        self.eixos.plot(valor_em_x, valor_em_y, color='red', marker='o', markersize=3)
        
        #print para testar iteração sobre a lista
        print('Valor da ação: U${0} \nDia: {1}'.format(valor_em_y, valor_em_x))
        plt.draw()
        self.canvas.show()

        label_alteravel= tk.Label(self, text= 'O preço da ação hoje é: U$ {0}'.format(valor_em_y),font=LARGE_FONT)
        label_alteravel.place(x=0,y=70)
        
        money_cliente= tk.Label(self, text= 'Seu saldo atual é de: {0}'.format(cliente.saldo))
        money_cliente.pack()
#        i.set('A ação está custando: {0}'.format(valor_em_y))
        i+= 1
'''DIFICULDADE MÉDIA'''    
#class modo_médio(tk.Frame): #dificuldade na qual cada ponto é plotado eixos cada 15 segundos, sendo este o
#                            #tempo para tomar eixos decisão de compra ou venda
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Gráficos", font=LARGE_FONT)
#        label.pack(pady=10,padx=10)
#
#        button1 = tk.Button(self, text="Voltar",command=lambda: controller.show_frame(MenuPage))
#        button1.pack()
#        
'''DIFICULDADE ALTA'''     
#class modo_difícil(tk.Frame):#dificuldade na qual cada ponto é plotado eixos cada 5 segundos, sendo este o
#                           #tempo para tomar eixos decisão de compra ou venda
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Gráficos", font=LARGE_FONT)
#        label.pack(pady=10,padx=10)
#
#        button1 = tk.Button(self, text="Voltar",command=lambda: controller.show_frame(MenuPage))
#        button1.pack()

#Atualizando a carteira Online:

carteiras={'carteiras':{'cliente':{'carteira':cliente.carteira, 'saldo':cliente.saldo}}}
firebase.patch('https://projeto-final-dessoft.firebaseio.com/', carteiras)

"""CONFIGURAÇÕES APP [/]"""
app = jogo()
app.geometry("1220x720")
app.mainloop()

"""FIM CONFIGURAÇÕES APP [/]"""
