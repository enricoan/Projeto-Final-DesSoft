# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:14:35 2018
controller
@author: Enrico Aloisi Nardi
"""

""""BIBLIOTECA [*]"""
#bibliotecas matplotlib
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
from classes import Cliente, Graficos
import funcoes as broker
from tkinter import *
from threading import Timer
from InfiniteTimer import InfiniteTimer
from firebase import firebase
import time

#importar o key_press_handler
from matplotlib.backend_bases import key_press_handler

""""FIM BIBLIOTECA [*]"""

""""FONTES PADRÃO E STYLE [0]"""
LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
style.use("ggplot")
""""FIM FONTES PADRÃO E STYLE [0]"""


""""FUNÇÕES UNIVERSAIS [1]"""
def instrucoes_popup():
    popup =tk.Tk()
    popup.wm_title("Instruções")
    with open('txts/' + 'Instrucoes.txt', 'r') as qpt3:
        dificuldade = qpt3.read()
    instrucao_label = tk.Label(popup, text=dificuldade)
    instrucao_label.pack()
    popup.mainloop()
""""FIM DEFINIÇÃO FUNÇÕES UNIVERSAIS [1]"""




"""DIFICULDADE [4]""" #página inicial do jogo: abre uma label grande com todas as instruções e botões 
                      #com os nomes das dificuldades
class TelaInicial(object):
    def __init__(self, parent):
        #super(TelaInicial, self).__init__(parent)
        self.controller = parent
        self.iniciarView()
        self.nome = "TELA_INICIAL"
        
        self.viewFacil      = modo_facil(self)
        self.viewFacil.geometry("1220x720")
        self.viewFacil.withdraw()

        self.viewMedio      = modo_medio(self)
        self.viewMedio.geometry("1220x720")
        self.viewMedio.withdraw()
         
        self.viewDificil    = modo_dificil(self)
        self.viewDificil.geometry("1220x720")
        self.viewDificil.withdraw()
        
        self.viewCurrent = None
        self.currentName = None
        
    def hide(self):
        """"""
        self.controller.withdraw()

    def show(self):
        """"""
        self.controller.update()
        self.controller.deiconify()
        
        
    def iniciarView(self):
        label_dificuldade = tk.Label(self.controller, text="Escolha a dificuldade", font=LARGE_FONT)
        label_dificuldade.place(x=0,y=0)
        
        button_dif1 = tk.Button(self.controller, text="Fácil", command=lambda:self.setCurrentView("FACIL"), font=NORMAL_FONT)
        button_dif1.pack(fill=tk.BOTH)
        
        button_dif2 = tk.Button(self.controller, text="Normal", command=lambda:self.setCurrentView("MEDIO"), font=NORMAL_FONT)
        button_dif2.pack(fill=tk.BOTH)
        
        button_dif3 = tk.Button(self.controller, text="Real",   command=lambda:self.setCurrentView("DIFICIL"), font=NORMAL_FONT)
        button_dif3.pack(fill=tk.BOTH)

        with open('txts/' + 'Instrucoes.txt', 'r') as qpt3:
            dificuldade = qpt3.read()
        instrucao_label = tk.Label(self.controller, text=dificuldade)
        instrucao_label.pack() 
        
    def setCurrentView(self, newViewName):
        newViewName = newViewName.upper()

        if(self.currentName == newViewName):
            return;

        if (self.currentName == "MEDIO" or self.currentName == "DIFICIL"):
            self.viewCurrent.timer_stop() 

        if (self.viewCurrent is not None):
            self.viewCurrent.hide()
            self.viewCurrent.reset()
            self.currentName = None
                        
        self.currentName = newViewName
       
        if("FACIL" == newViewName):
            self.viewCurrent    = self.viewFacil
        elif("MEDIO" == newViewName):
            self.viewCurrent = self.viewMedio
        elif("DIFICIL" == newViewName):
            self.viewCurrent = self.viewDificil
        else:
            return

        self.viewCurrent.show()
        
        
"""FIM DIFICULDADE [4]"""

cliente_facil=Cliente()
class modo_facil(tk.Toplevel): #modo do jogo no qual eixos pessoa clica no botão e o valor da ação é plotado

    def __init__(self, parent, manual = True):
        super(modo_facil, self).__init__()
        self.controller = parent
        self.voltar = None
        self.tempo  = []
        self.valores_acoes = []
        self.carregado = False        
        self.idx = 0
        self.linkedValue = DoubleVar()
        self.cliente =  Cliente() 
        self.iniciarView(manual)
        self.nome = "FACIL"
        
    def iniciarView(self, manual = True):
       
        #labels da página
        titulo_pagina = tk.Label(self, text="CONTROLE DE PREÇOS", font=LARGE_FONT)
        titulo_pagina.pack()
        
        #botões da página
        self.voltar= tk.Button(self, text="Voltar", command = lambda:self.controller.setCurrentView("TELA_INICIAL"))
        self.voltar.place(x=1000,y=0)
        
        # No modo facil os pontos sao plotados manualmente
        if (manual):
            plotador = tk.Button(self, text= 'Plotar mais um ponto', command = lambda:self.proximo_ponto())
            plotador.place(x=950, y=30)
       
        botao_comprar = tk.Button(self, text="Comprar", \
                                command= lambda: broker.buy(cliente_facil,'AAPL',\
                                float(self.valores_acoes[self.idx]), self.linkedValue, quantidade= 100))
        botao_comprar.place(x=500, y=90)

        botao_vender = tk.Button(self, text="Vender", \
                                 command= lambda: broker.sell(cliente_facil,'AAPL',float \
                                (self.valores_acoes[self.idx]), self.linkedValue, quantidade= 100))
        botao_vender.place(x=550, y=90)
        

        progresso= ttk.Progressbar(self, orient=tk.HORIZONTAL, length=420, mode="determinate", maximum=1E6, variable = self.linkedValue)
        progresso.place(x=400,y=600)
        
        label_empresa= tk.Label(self, text= 'Escolha a empresa na qual quer investir', font= LARGE_FONT)
        label_empresa.place(x=0,y=0)
        
        #lista com as empresas que podem ser escolhidas pelo usuário
 
        self.listboxEmpresas = tk.Listbox(self)

        self.listboxEmpresas.bind('<<ListboxSelect>>', self.CurSelect)
        
        self.listboxEmpresas.place(x=4,y=20)
        self.list = ['AAPL', 'ACN', 'ADBE', 'AVGO', 'BIDU', 'BTI', 'BUD', 'CHL', 'CL', \
                     'CRM', 'CSCO', 'DEO', 'ECL', 'EL', 'F', 'FB', 'GM', 'GOOG (1)', \
                     'GOOGL (1)', 'HMC', 'IBM', 'INTC', 'KO', 'MDLZ', 'MO', 'MSFT (2)', \
                     'MU', 'NKE', 'NVDA', 'ORCL', 'PEP', 'PHG', 'PM', 'QCOM', 'SAP', \
                     'SNE', 'STZ', 'T', 'TM', 'TMUS', 'TSLA', 'TSM', 'TXN', 'UL', 'UN', 'VMW', 'VZ']
        
        for item in self.list:
            self.listboxEmpresas.insert(END, item)
            
        #tudo o que precisamos para o gráfico atualizável
        fig = Figure(figsize=(5,4), dpi=100)
        self.eixos = fig.add_subplot(1,1,1)
        self.canvas = FigureCanvasTkAgg(fig, self)
        self.widget = self.canvas.get_tk_widget()
        self.eixos.set_autoscale_on(True)
        self.eixos.set_xlabel('Tempo (dias)')
        self.eixos.set_ylabel('Valor da ação (dólares)')
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
        self.canvas._tkcanvas.pack(padx=400, side=tk.LEFT)
        self.protocol("WM_DELETE_WINDOW", lambda: self.controller.setCurrentView("TELA_INICIAL"))
        
    def hide(self):
        """"""
        self.listboxEmpresas.unbind('<<ListboxSelect>>')
        self.withdraw()

    def show(self):
        """"""
        self.update()
        self.deiconify()
        self.listboxEmpresas.bind('<<ListboxSelect>>', self.CurSelect)
        
    def reset(self):
        #self.idx = 0
        #self.eixos.cla()
        self.canvas.show()
 
        
       #a pesquisa para as empresas
    def CurSelect(self, event):
        self.eixos.cla()
        self.canvas.show()
        widget = event.widget
        selection = widget.curselection()
        picked = widget.get(selection[0])
        self.tempo, self.valores_acoes = broker.geradordeserie(picked)
        self.idx = 0
        self.carregado = True

        # return self.tempo, self.valores_acoes
    
    def proximo_ponto(self):
        if (not self.carregado):
            return
        
        if (self.idx >= len(self.tempo)):
            self.timer_stop()
            return
        
        self.eixos.set_xlabel('Tempo (dias)') 
        self.eixos.set_ylabel('Valor da ação (dólares)')
        
        valor_em_x = self.tempo[self.idx]
        valor_em_y = self.valores_acoes[self.idx]
        
        #por extenso e com diametro do ponto
        self.eixos.plot(valor_em_x, valor_em_y, color='r', marker='o', markersize=3)
        
        # plt.draw()
        self.canvas.show()        
#        print para testar iteração sobre a lista
        print('Valor da ação: U${0} \nDia: {1}'.format(valor_em_y, valor_em_x))

        label_alteravel= tk.Label(self, text= 'O preço da ação hoje é: U$ {0}'.format(valor_em_y), font=LARGE_FONT)
        label_alteravel.place(x=0,y=500)
        
        money_cliente= tk.Label(self, text= 'Seu saldo atual é de: {0}'.format(cliente_facil.saldo), font=LARGE_FONT)
        money_cliente.place(x=0,y=600)
        self.idx += 1

class modo_medio(modo_facil):
    def __init__(self, parent):
        super(modo_medio, self).__init__(parent, False)
        # modo_facil.__init__(self, parent, controller, False)
        self.period = IntVar() # tkInter atualiza automaticamente
        self.period.set(15)
        
        self.currentPeriod = self.period.get()
        
        labelFrame = tk.Frame(self)
        tk.Label(labelFrame, text="Período(milisegundos)").grid(row=0, column=0)
        tk.Entry(labelFrame, width=10, textvariable=self.period).grid(row=0, column=2)
        labelFrame.place(x=800,y=105)
        
        self.buttonIniciar= tk.Button(self, text="Iniciar", command = lambda:self.timer_start(), state=DISABLED)
        self.buttonIniciar.place(x=1000,y=100)
        #botões da página
        self.buttonParar= tk.Button(self, text="Parar", command = lambda:self.timer_stop(), state=DISABLED)
        self.buttonParar.place(x=1000,y=150)

        self.plotTimer = InfiniteTimer(self.currentPeriod, lambda:self.proximo_ponto())
        self.nome = "MEDIO"

    def CurSelect(self, event):
        super(modo_medio, self).CurSelect(event)
        # modo_facil.CurSelect(self, event)

        # somente habilita os botoes se houver carregado algum arquivo
        self.buttonIniciar.config(state=NORMAL) 
        self.buttonParar.config(state=NORMAL)
       
    def timer_start(self):
        if (not self.carregado):
            return
        
        if (self.currentPeriod != self.period.get()):
            self.currentPeriod = self.period.get()
            self.plotTimer.cancel()
            self.plotTimer.destroy()
            self.plotTimer = InfiniteTimer(self.currentPeriod, lambda:self.proximo_ponto())

        self.plotTimer.start()
        
    def timer_stop(self):
        self.plotTimer.cancel()
            
class modo_dificil(modo_medio):
    def __init__(self, parent):
        # modo_medio.__init__(self, parent, controller)
        super(modo_dificil, self).__init__(parent)
        self.period.set(5)            
        self.nome = "DIFICIL"
            
""""CONFIGURAÇÕES TKINTER [2]"""
class Jogo(object):
    def __init__(self, parent):
        self.root = parent
        self.root.title("Million Run")

        #inicializador tkinter
        self.container = tk.Frame(parent)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.pack()
        
        menu = tk.Menu(self.container)
        tk.Tk.config(self.root, menu=menu)

        subMenu = tk.Menu(menu)
        menu.add_cascade(label='Jogo', menu=subMenu)
        subMenu.add_command(label="Salvar Jogo")
        subMenu.add_command(label="Carregar Jogo")

        instrucoesMenu = tk.Menu(menu)
        menu.add_cascade(label='Instruções', menu=instrucoesMenu)
        instrucoesMenu.add_command(label="Guia para Iniciantes", command=instrucoes_popup)
     
        self.telaInicial   = TelaInicial(parent)
        self.telaInicial.show()
        
    def hide(self):
        """"""
        self.root.withdraw()

    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()
    
""""CONFIGURAÇÕES TKINTER [2]"""


"""CONFIGURAÇÕES APP [/]"""

def main():
    root = tk.Tk()
    #root.geometry("1220x720")
    app = Jogo(root)
    root.mainloop()
  
if __name__ == "__main__":
    main()

"""FIM CONFIGURAÇÕES APP [/]"""
