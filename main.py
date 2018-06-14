# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:14:35 2018

@author: Enrico Aloisi Nardi
"""

""""BIBLIOTECA [*]"""
#bibliotecas matplotlib
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.pyplot as plt
#Bibliotecas tkinter
import tkinter as tk
import tkinter.ttk as ttk

import classes as c
from modo_facil import modo_facil

import funcoes as f
import time

#importar o key_press_handler
from matplotlib.backend_bases import key_press_handler

cliente= c.Clientes()
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
    with open('Instrucoes.txt', 'r') as qpt3:
        dificuldade = qpt3.read()
    instrucao_label = tk.Label(popup, text=dificuldade)
    instrucao_label.pack()
    popup.mainloop()
""""FIM DEFINIÇÃO FUNÇÕES UNIVERSAIS [1]"""

""""CONFIGURAÇÕES TKINTER [2]"""
m=0 #contador do timer 
class jogo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Tk.wm_title(self, "Million Run")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight=1)
        
        menu = tk.Menu(container)
        tk.Tk.config(self, menu=menu)

        subMenu = tk.Menu(menu)
        menu.add_cascade(label='Jogo', menu=subMenu)
        subMenu.add_command(label="Salvar Jogo")
        subMenu.add_command(label="Carregar Jogo")

        instrucoesMenu = tk.Menu(menu)
        menu.add_cascade(label='Instruções', menu=instrucoesMenu)
        instrucoesMenu.add_command(label="Guia para Iniciantes", command=instrucoes_popup)

        self.frames = {}
        # que poha é essa aqui?
        for F in (Difficulty, Game, modo_facil, modo_medio, modo_dificil):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Difficulty)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def timer(self):
        global m
        if m < 1260:
            new_time = time.get() + 1
            time.set(new_time)
            
            self.eixos.set_xlabel('Tempo (dias)')
            self.eixos.set_ylabel('Valor da ação (dólares)')
    
            valor_em_x = tempo[k] #mudança da variável que é utilizada como indice da lista que será plotada
                                    #agora é uma variável usada só pela função timer
            valor_em_y = valores_acoes[k]
            
            #por extenso e com diametro do ponto
            self.eixos.plot(valor_em_x, valor_em_y, color='r', marker='o', markersize=3)
            
            plt.draw()
            self.canvas.show()
            
            #print para testar iteração sobre a lista
            print('Valor da ação: U${0} \nDia: {1}'.format(valor_em_y, valor_em_x))
    
            label_alteravel= tk.Label(self, text= 'O preço da ação hoje é: U$ {0}'.format(valor_em_y),font=LARGE_FONT)
            label_alteravel.place(x=0,y=80)
            
            money_cliente= tk.Label(self, text= 'Seu saldo atual é de: {0}'.format(cliente.saldo))
            money_cliente.place(x=0,y=600)
            
            self.after(100, self.timer) # linha que supostamente chama a função timer e atualiza o gráfico após um 
                                        #determinado intervalo de tempo
            print(k)
            m += 1
""""CONFIGURAÇÕES TKINTER [2]"""

"""DIFICULDADE [4]"""
class Difficulty(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label_dificuldade = tk.Label(self, text="Escolha a dificuldade", font=LARGE_FONT)
        label_dificuldade.place(x=0,y=0)
        
        button_dif1 = tk.Button(self, text="Fácil",command=lambda:controller.show_frame(modo_facil), font=NORMAL_FONT)
        button_dif1.pack(fill=tk.BOTH)
        
        button_dif2 = tk.Button(self, text="Normal",command=lambda:controller.show_frame(modo_médio), font=NORMAL_FONT)
        button_dif2.pack(fill=tk.BOTH)
        
        button_dif3 = tk.Button(self, text="Real", font=NORMAL_FONT, command=lambda:controller.show_frame(modo_difícil))
        button_dif3.pack(fill=tk.BOTH)

        with open('Instrucoes.txt', 'r') as qpt3:
            dificuldade = qpt3.read()
        instrucao_label = tk.Label(self, text=dificuldade)
#        instrucao_label
        instrucao_label.pack()
        
        
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

        total = tk.Label(self, text="Total: {0}".format(cliente.saldo), font=NORMAL_FONT)
        total.place(x=1100, y=650)
""""FIM JOGO [4]"""

""""PÁGINA GRÁFICO [6] // TESTE"""
tempo= []
valores_acoes=[]
i=0
#easymode= modo_facil(parent,controller)
 
'''DIFICULDADE ALTA'''   

# que poha é essa aqui? que poha é tk.Frame?
  
class modo_dificil(tk.Frame):#dificuldade na qual cada ponto é plotado eixos cada 5 segundos, sendo este o
                             #tempo para tomar eixos decisão de compra ou venda
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        photo = tk.PhotoImage(file='cash.png')
        BGlabel = tk.Label(self, image=photo)
        BGlabel.image = photo
        BGlabel.place(x=0, y=0)
        
        listbox = tk.Listbox(self)
        listbox.place(x=0,y=0)
        for item in ['AAPL', 'ACN', 'ADBE', 'AVGO', 'BIDU', 'BTI', 'BUD', 'CHL', 'CL', 'CRM', 'CSCO', 'DEO', 'ECL', 'EL', 'F', 'FB', 'GM', 'GOOG (1)', 'GOOGL (1)', 'HMC', 'IBM', 'INTC', 'KO', 'MDLZ', 'MO', 'MSFT (2)', 'MU', 'NKE', 'NVDA', 'ORCL', 'PEP', 'PHG', 'PM', 'QCOM', 'SAP', 'SNE', 'STZ', 'T', 'TM', 'TMUS', 'TSLA', 'TSM', 'TXN', 'UL', 'UN', 'VMW', 'VZ']:
            listbox.insert(END, item)
        
        label = tk.Label(self, text="Gráficos", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        voltar = tk.Button(self, text="Voltar",command=lambda: controller.show_frame(Difficulty))
        voltar.pack() 

        botao_comprar = tk.Button(self, text="Comprar", command= lambda: f.buy(cliente,'AAPL',valores_acoes[i], quantidade= 100))
        botao_comprar.place(x=500, y=90)

        botao_vender = tk.Button(self, text="Vender", command= lambda: f.sell(cliente,'AAPL',valores_acoes[i], quantidade= 100))
        botao_vender.place(x=550, y=90)
        
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

        tempo,valores_acoes= f.geradordeserie('TSLA')
        
"""CONFIGURAÇÕES APP [/]"""
app = jogo()
app.geometry("1220x720")
app.mainloop()
app.timer()


"""FIM CONFIGURAÇÕES APP [/]"""
