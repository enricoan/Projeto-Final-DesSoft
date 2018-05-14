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
import matplotlib.pyplot as plt
#Bibliotecas tkinter
import tkinter as tk
from tkinter import ttk

from classes import Clientes
import funcoes as f
""""FIM BIBLIOTECA [*]"""

cliente= Clientes()

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
    label = ttk.Label(popup, text= "batata", font = LARGE_FONT)
    label.pack(side="top", fill = "x", pady= 10)
    B1 = ttk.Button(popup, text = "Okay", command = popup.destroy())
    B1.pack()
    popup.mainloop()

""""FIM DEFINIÇAO FUNÇÕES UNIVERSAIS [1]"""


""""CONFIGURAÇOES TKINTER [2]"""

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

""""CONFIGURAÇOES TKINTER [2]"""

""""MENU [3]"""
class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Menu!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button = ttk.Button(self, text="Jogar!",
                            command=lambda: controller.show_frame(Dificulty))
        button.pack()

        button3 = ttk.Button(self, text="Visit Graph Page",
                            command=lambda: controller.show_frame(modo_facil))
        button3.pack()
""""FIM MENU [3]"""
"""DIFICULDADE [4]"""
class Dificulty(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label_dificuldade = tk.Label(self, text="Escolha a dificuldade", font=LARGE_FONT)
        button_dif1 = tk.Button(self, text="Fácil", font=NORMAL_FONT)
        button_dif1.pack()
        button_dif2 = tk.Button(self, text="NORMAL", 
                                command=lambda:controller.show_frame(modo_facil), font=NORMAL_FONT)
        button_dif2.pack()
        button_dif3 = tk.Button(self, text="Real", font=NORMAL_FONT)
        button_dif3.pack()
        button = ttk.Button(self, text="Voltar para Home!",
                            command=lambda: controller.show_frame(MenuPage))
        button.pack()
"""FIM DIFICULDADE [4]"""

""""JOGO [5]"""
class Game(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        one = tk.Label(self, text="Million Run")

        one.place(x=1280 / 2, y=0)

        carteira = tk.Label(self, text="Carteira", font=LARGE_FONT)

        carteira.place(x=1100, y=100)

        obtidos_texto = "Microsoft,\n Sony,\n LG"
        obtidos = tk.Label(self, text=obtidos_texto, font=NORMAL_FONT)

        obtidos.place(x=1100, y=150)
        
        botao_comprar = tk.Button(self, text="Vender", command= lambda: f.buy(cliente,'tesla',valores_ações[i], quantidade= 100))
        botao_comprar.place(x=400, y=450)

        botao_vender = tk.Button(self, text="Comprar", command= lambda: f.sell(cliente,'tesla',valores_ações[i], quantidade= 100))
        botao_vender.place(x=400, y=500)

        grafico = tk.Label(self, text="Grafico")
        grafico.place(x=200, y=475)

        total = tk.Label(self, text="Total: {0}".format(cliente.saldo), font=NORMAL_FONT)
        total.place(x=1100, y=650)
        
        button1 = ttk.Button(self, text="Voltar",command=lambda: controller.show_frame(MenuPage))
        button1.pack()
        
        
""""FIM JOGO [4]"""



""""PÁGINA GRÁFICO [6] // TESTE"""
lista_adição= []
tempo_adição= []
tempo = []
valores_ações=[] 
i=0
class modo_facil(tk.Frame): #modo do jogo no qual a pessoa clica no botão e o valor da ação é plotado

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",command=lambda: controller.show_frame(MenuPage))
        button1.pack()
        
        button2 = ttk.Button(self, text= 'Plotar mais um ponto', command= self.proximo_ponto)
        button2.pack()
        
#        style.use('seaborn-whitegrid')
        
        f = Figure(figsize=(5,5), dpi=300)
        a= f.add_subplot(111)
        
        
        
        canvas = FigureCanvasTkAgg(f, self)
        self.toolbar = NavigationToolbar2TkAgg(canvas, self)
        self.widget = canvas.get_tk_widget()

        a.set_autoscale_on(True)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    with open('teslateste - Copia - Copia.txt','r') as arquivo:
        valorescsv = arquivo.read()
    linhas= valorescsv.split('\n')
    for linha in linhas:
        x,y= linha.split(',')
        tempo.append(int(x))
        valores_ações.append(int(y))
    
    
    def proximo_ponto(self):
        global i
                
        f = Figure(figsize=(5,5), dpi=300)
        a= f.add_subplot(111)
        canvas= FigureCanvasTkAgg(f, self)
        
        a.set_xlabel('Tempo (dias)')
        a.set_ylabel('Valor da ação')
        lista_adição.append(valores_ações[i])
        tempo_adição.append(tempo[i])
        
#        a.plot(tempo[i],valores_ações[i])
        print('Valor da ação: U${0} \nDia: {1}'.format(valores_ações[i],tempo[i]))
        plt.draw()
        canvas.show()
        i+= 1

#class modo_médio(tk.Frame): #dificuldade na qual cada ponto é plotado a cada 15 segundos, sendo este o
#                            #tempo para tomar a decisão de compra ou venda
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Gráficos", font=LARGE_FONT)
#        label.pack(pady=10,padx=10)
#
#        button1 = ttk.Button(self, text="Voltar",command=lambda: controller.show_frame(MenuPage))
#        button1.pack()
#        
#        
#class modo_difícil(tk.Frame):#dificuldade na qual cada ponto é plotado a cada 5 segundos, sendo este o
#                           #tempo para tomar a decisão de compra ou venda
#    def __init__(self, parent, controller):
#        tk.Frame.__init__(self, parent)
#        label = tk.Label(self, text="Gráficos", font=LARGE_FONT)
#        label.pack(pady=10,padx=10)
#
#        button1 = ttk.Button(self, text="Voltar",command=lambda: controller.show_frame(MenuPage))
#        button1.pack()
        
        
""""PÁGINA GRÁFICO [6] // TESTE"""



"""CONFIGURAÇõES APP [/]"""
app = jogo()
app.geometry("1000x700")
app.mainloop()

"""FIM CONFIGURAÇõES APP [/]"""