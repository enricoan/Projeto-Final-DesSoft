# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 11:28:42 2018

@author: Enrico Aloisi Nardi
"""

import matplotlib.pyplot as plt
from matplotlib import style

style.use('seaborn-whitegrid')
tempo = []
valores_ações=[]
valores_acoes= open('tesla teste - Copia.txt','r').read()
linhas= valores_acoes.split('\n')
for linha in linhas:
    x,y= linha.split(',')
    tempo.append(int(x))
    valores_ações.append(int(y))

fig= plt.plot(tempo,valores_ações)
plt.xlabel('Tempo (dias)')
plt.ylabel('Valor da ação')

plt.grid(True)
plt.show()

#%%
""""BIBLIOTECAS [*]"""

#bibliotecas matplotlib
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.pyplot as plt
from matplotlib import style
import os
#Bibliotecas tkinter
import tkinter as tk
from tkinter import ttk

""""FIM BIBLIOTECAS [*]"""


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

def buy():
    print("Item Comprado Com sucesso!")

def sell():
    print("Item Vendido Com sucesso!")

def wallet():
    print("Microsoft,Facebook,Google,Apple")

""""FIM DEFINIÇÂO FUNÇÕES UNIVERSAIS [1]"""


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

        for F in (MenuPage, Game, Credits, PageThree, ScoreBoard):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MenuPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

"""" FIM CONFIGURAÇOES TKINTER [2]"""


""""MENU [3]"""

class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Menu!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)


        button = ttk.Button(self, text="Jogar!",
                            command=lambda: controller.show_frame(Game))

        button.pack()

        button2 = ttk.Button(self, text="Créditos",
                            command=lambda: controller.show_frame(Credits))
        button2.pack()

        button3 = ttk.Button(self, text="Visit Graph Page",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()

        button4 = ttk.Button(self, text = "Ver Placar de Líderes",
                             command=lambda: controller.show_frame(ScoreBoard))
        button4.pack()

""""FIM MENU [3]"""


""""JOGO [4]"""

class Game(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Million RUN!", font=LARGE_FONT)
        label.grid(pady=10,padx=10)
        carteira_texto = "Microsoft,Facebook,Google,Apple"
        button1 = ttk.Button(self, text="Voltar para HOME",
                            command=lambda: controller.show_frame(MenuPage))

        button1.grid()
        botao_comprar = ttk.Button(self, text="Buy",
                                   command=buy)
        botao_comprar.grid()
        botao_vender = ttk.Button(self, text="Sell",
                                  command=sell)
        botao_vender.grid()
        carteira_objeto = tk.Label(self, text="Carteira:")
        carteira_objeto.grid()
        carteira = tk.Label(self, text=carteira_texto, font=SMALL_FONT)
        carteira.grid()

""""FIM JOGO [4]"""


""""CRÉDITOS [5]"""

class Credits(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        titulo = tk.Label(self, text="Créditos", font=LARGE_FONT)
        titulo.pack(pady=10,padx=10)

        texto_creditos = "Enrico:blablabla\nGuilherme:Blablabla\nJadson:blablabla"
        creditos = tk.Label(self, text=texto_creditos, font=NORMAL_FONT)
        creditos.pack()
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MenuPage))

        button1.pack()

""""FIM CRÉDITOS [5]"""


""""PÁGINA GRÁFICO [6] // TESTE"""
lista_adição=[]
tempo_adição=[]

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MenuPage))
        button2 = ttk.Button(self, text= 'Plotar mais um ponto', command= self.proximo_ponto)
        
        button1.pack()
        button2.pack()
        
        style.use('seaborn-whitegrid')
        tempo = []
        valores_ações=[]
        THIS_FOLDER = os.path.dirname(os.path.abspath('__file__'))
        valores_ações = os.path.join(THIS_FOLDER, 'teslateste - Copia.txt')
        linhas= valores_acoes.split('\n')
        for linha in linhas:
            x,y= linha.split(',')
            tempo.append(int(x))
            valores_ações.append(int(y))
        
        f = Figure(figsize=(3,3), dpi=100)
        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        
    def proximo_ponto(self):
        global i
        lista_adição.append(valores_ações[i])
        tempo_adição.append(tempo[i])
        plt.plot(tempo_adição,lista_adição)
        i+= 1
        print (i)
""""FIM PÁGINA GRÁFICO [6]"""


"""PLACARES [7]"""

class ScoreBoard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        placar_texto = "1o - Enrico\n2o - Jadson\n 3o - Guilherme"
        placar = tk.Label(self, text=placar_texto, font=NORMAL_FONT)
        placar.pack()
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MenuPage))

        button1.pack()

"""FIM PLACARES [7]"""


"""CONFIGURAÇõES APP [/]"""

app = jogo()
app.geometry("1280x720")
app.mainloop()

"""FIM CONFIGURAÇõES APP [/]"""
