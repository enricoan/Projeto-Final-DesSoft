# -*- coding: utf-8 -*-
"""
Created on Thu May 24 08:40:58 2018

@author: Enrico Aloisi Nardi
"""
import tkinter as tk
valores_acoes=[]
tempo=[]
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from classes import Clientes

cliente= Clientes()
class modo_facil(tk.Frame): #modo do jogo no qual eixos pessoa clica no botão e o valor da ação é plotado
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #labels da página
        titulo_pagina = tk.Label(self, text="CONTROLE DE PREÇOS", font=LARGE_FONT)
        titulo_pagina.pack()
        
        #botões da página
        voltar= tk.Button(self, text="Voltar",command=lambda: controller.show_frame(Difficulty))
        voltar.place(x=1000,y=0)
        
        plotador = tk.Button(self, text= 'Plotar mais um ponto', command= self.proximo_ponto)
        plotador.place(x=950,y=30)
        
        botao_comprar = tk.Button(self, text="Vender", command= lambda: f.buy(cliente,'AAPL',float(valores_acoes[i]), quantidade= 100))
        botao_comprar.place(x=500, y=90)

        botao_vender = tk.Button(self, text="Comprar", command= lambda: f.sell(cliente,'AAPL',float(valores_acoes[i]), quantidade= 100))
        botao_vender.place(x=550, y=90)
        
        progresso= ttk.Progressbar(self, orient=tk.HORIZONTAL, length=500, mode="determinate", maximum=1E6, value= cliente.saldo)
        progresso.place(x=0,y=100)
        
        label_empresa= tk.Label(self, text= 'Escolha a empresa na qual quer investir', font= LARGE_FONT)
        label_empresa.place(x=0,y=0)
        
        #lista com as empresas que podem ser escolhidas pelo usuário
        listbox= tk.Listbox(self)
        listbox.config(width=0,height=0)
        listbox.bind('<<ListboxSelect>>',self.CurSelect)
        listbox.place(x=0,y=20)
        for item in ['AAPL', 'ACN', 'ADBE', 'AVGO', 'BIDU', 'BTI', 'BUD', 'CHL', 'CL', 'CRM', 'CSCO', 'DEO', 'ECL', 'EL', 'F', 'FB', 'GM', 'GOOG (1)', 'GOOGL (1)', 'HMC', 'IBM', 'INTC', 'KO', 'MDLZ', 'MO', 'MSFT (2)', 'MU', 'NKE', 'NVDA', 'ORCL', 'PEP', 'PHG', 'PM', 'QCOM', 'SAP', 'SNE', 'STZ', 'T', 'TM', 'TMUS', 'TSLA', 'TSM', 'TXN', 'UL', 'UN', 'VMW', 'VZ']:
            listbox.insert(END, item)
            
        #tudo o que precisamos para o gráfico atualizável
        fig = Figure(figsize=(5,4), dpi=100)
        self.eixos = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, self)
        self.widget = self.canvas.get_tk_widget()
        self.eixos.set_autoscale_on(True)
        self.eixos.set_xlabel('Tempo (dias)')
        self.eixos.set_ylabel('Valor da ação (dólares)')
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
        self.canvas._tkcanvas.pack(side=tk.LEFT)

       #a pesquisa para as empresas
    def CurSelect(self,event):
        selection=curselection()
        picked = get(selection[0])
        tempo,valores_acoes= f.geradordeserie(picked)
            
    def proximo_ponto(self):
        global i
#        self.eixos.set_title('{0}'.format(cb.get()))
        self.eixos.set_xlabel('Tempo (dias)')
        self.eixos.set_ylabel('Valor da ação (dólares)')

        valor_em_x = tempo[i]
        valor_em_y = valores_acoes[i]
        
        #por extenso e com diametro do ponto
        self.eixos.plot(valor_em_x, valor_em_y, color='r', marker='o', markersize=3)
        
        plt.draw()
        self.canvas.show()        
#        print para testar iteração sobre a lista
        print('Valor da ação: U${0} \nDia: {1}'.format(valor_em_y, valor_em_x))

        label_alteravel= tk.Label(self, text= 'O preço da ação hoje é: U$ {0}'.format(valor_em_y),font=LARGE_FONT)
        label_alteravel.place(x=0,y=80)
        
        money_cliente= tk.Label(self, text= 'Seu saldo atual é de: {0}'.format(cliente.saldo))
        money_cliente.place(x=0,y=600)
        i+= 1