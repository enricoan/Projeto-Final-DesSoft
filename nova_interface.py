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
#from matplotlib import style
import matplotlib.pyplot as plt
#Bibliotecas tkinter
import tkinter as tk
import tkinter.ttk as ttk
from classes import Clientes
import funcoes as f
#from firebase import firebase
import time
#importar o key_press_handler
from matplotlib.backend_bases import key_press_handler

""""FIM BIBLIOTECA [*]"""

""""FireBase[/*\]"""
#Criando o objeto 'cliente' e atribuindo-lhe dados disponíveis no firebase

#firebase=firebase.FirebaseApplication('https://projeto-final-dessoft.firebaseio.com/', None)
#carteiras= firebase.get('carteiras', None)
#cliente=Clientes()
#cliente.carteira=carteiras['cliente']['carteira']
#cliente.saldo=carteiras['cliente']['saldo']

""""FIM FireBase[/*\]"""

#importar o key_press_handler
from matplotlib.backend_bases import key_press_handler

cliente= Clientes()

""""FONTES PADRÃO E STYLE [0]"""
LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
style.use("ggplot")
""""FIM FONTES PADRÃO E STYLE [0]"""


""""FUNÇÕES UNIVERSAIS [1]"""
#PopUp Instruções
def instrucoes_popup():
    popup =tk.Tk()
    popup.wm_title("Instruções")
    with open('Instrucoes.txt', 'r') as entrada_instrucoes:
        dificuldade = entrada_instrucoes.read()
    instrucao_label = tk.Label(popup, text=dificuldade)
    instrucao_label.pack()
    popup.mainloop()

#Click do Mouse
def on_select(event=None):        
    print("passou por aqui 2!!!!!!!!!!!!!!!!")
    if event:
        print(event.widget.get())


""""FIM DEFINIÇÃO FUNÇÕES UNIVERSAIS [1]"""


""""CONFIGURAÇÕES TKINTER [2]"""

class jogo(tk.Tk) #Default config para todas as paginas:
    def __init__(self, *args, **kwargs):
        #Inicializador Tk.Tk(window)
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Million Run")

        #Criar Container para gerar Frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight=1)

        #Criar ToolBar (Adicionar ToolBar ao Container(Frame Principal)
        menu = tk.Menu(container)
        tk.Tk.config(self, menu=menu)

        #Criar SubMenu "JOGO"
        subMenu = tk.Menu(menu)
        menu.add_cascade(label='Jogo', menu=subMenu)
        subMenu.add_command(label="Salvar Jogo")
        subMenu.add_command(label="Carregar Jogo")

        #Criar SubMenu "Instruções
        instrucoesMenu = tk.Menu(menu)
        menu.add_cascade(label='Instruções', menu=instrucoesMenu)
        instrucoesMenu.add_command(label="Guia para Iniciantes", command=instrucoes_popup)

        #Criar Dicionario com as Frames disponíveis para Container
        self.frames = {}
        #Loop que percorre Classes(Páginas Disponíveis)
        for F in (Difficulty, Game, modo_facil, modo_difícil, modo_médio):
            #Dizer que frame = container
            frame = F(container, self)
            #Adicionar ao dicionario frames o frame criado
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        #inicializa o jogo na pagina Difficulty
        self.show_frame(Difficulty)

    def doNothing(self):
        tk.END()
    #Levantar apenas a pagina selecionada
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


""""CONFIGURAÇÕES TKINTER [2]"""

"""DIFICULDADE [4]"""
class Difficulty(tk.Frame):
    def __init__(self, parent, controller):
        # Inicializador Tk.Tk(window)
        tk.Frame.__init__(self, parent)
        #PRINTAR ESCOLHER DIFICULDADES
        dificuldade_label = tk.Label(self, text="Escolha a dificuldade", font=LARGE_FONT)
        dificuldade_label.place(x=0,y=0)

        #CRIAR BOTÕES DAS DIFICULDADES
        dif1_button = tk.Button(self, text="Fácil",command=lambda:controller.show_frame(modo_facil), font=NORMAL_FONT)
        dif1_button.pack(fill=tk.BOTH)
        
        dif2_button = tk.Button(self, text="Normal",command=lambda:controller.show_frame(modo_médio), font=NORMAL_FONT)
        dif2_button.pack(fill=tk.BOTH)
        
        dif3_button = tk.Button(self, text="Real", font=NORMAL_FONT, command=lambda:controller.show_frame(modo_difícil))
        dif3_button.pack(fill=tk.BOTH)
        
        home_button = tk.Button(self, text="Voltar para Home",command=lambda: controller.show_frame(Difficulty))
        home_button.pack(fill=tk.BOTH)

        #Adicionar Instruções a pagina
        with open('Instrucoes.txt', 'r') as entrada_instrucoes:
            dificuldade = entrada_instrucoes.read()

        instrucao_label = tk.Label(self, text=dificuldade)
        instrucao_label.pack()
        
        
"""FIM DIFICULDADE [4]"""

""""JOGO [5]"""
class Game(tk.Frame):
    def __init__(self, parent, controller):
        # Inicializador Tk.Tk(window)
        tk.Frame.__init__(self, parent)
        #PRINTAR MILLION RUN
        millionrun_label = tk.Label(self, text="Million Run")
        millionrun_label.place(x=1280 / 2, y=0)
        #PRINTAR CARTEIRA
        carteira = tk.Label(self, text="Carteira", font=LARGE_FONT)
        carteira.place(x=1100, y=100)
        
        comprar_button = tk.Button(self, text="Comprar", command= lambda: f.buy(cliente,'tesla',valores_acoes[i], quantidade= 100))
        comprar_button.place(x=400, y=450)

        vender_button = tk.Button(self, text="Vender", command= lambda: f.sell(cliente,'tesla',valores_acoes[i], quantidade= 100))
        vender_button.place(x=400, y=500)

        grafico = tk.Label(self, text="Grafico")
        grafico.place(x=200, y=475)

        total = tk.Label(self, text="Total: {0}".format(cliente.saldo), font=NORMAL_FONT)
        total.place(x=1100, y=650)
""""FIM JOGO [4]"""

""""PÁGINA GRÁFICO [6] // TESTE"""
tempo = []
valores_acoes=[] 
i=0
class modo_facil(tk.Frame): #modo do jogo no qual eixos pessoa clica no botão e o valor da ação é plotado
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #labels da página
        titulo_pagina = tk.Label(self, text="CONTROLE DE PREÇOS", font=LARGE_FONT, underline=1)
        titulo_pagina.pack()
        
        #botões da página
        voltar= tk.Button(self, text="Voltar",command=lambda: controller.show_frame(Difficulty))
        voltar.place(x=1000,y=0)
        
        plotador = tk.Button(self, text= 'Plotar mais um ponto', command= self.proximo_ponto)
        plotador.place(x=950,y=30)
        
        #barra de pesquisa para as empresas
        cb= ttk.Combobox(parent, values=('AAPL', 'ACN', 'ADBE', 'AVGO', 'BIDU', 'BTI', 'BUD', 'CHL', 'CL', 'CRM', 'CSCO', 'DEO', 'ECL', 'EL', 'F', 'FB', 'GM', 'GOOG (1)', 'GOOGL (1)', 'HMC', 'IBM', 'INTC', 'KO', 'MDLZ', 'MO', 'MSFT (2)', 'MU', 'NKE', 'NVDA', 'ORCL', 'PEP', 'PHG', 'PM', 'QCOM', 'SAP', 'SNE', 'STZ', 'T', 'TM', 'TMUS', 'TSLA', 'TSM', 'TXN', 'UL', 'UN', 'VMW', 'VZ'))
        cb.place(x=0,y=0)
        cb.set('AAPL')   
        cb.bind('<<ComboboxSelected>>', on_select)
        print("Passou por aqui")

        comprar_button = tk.Button(self, text="Vender", command= lambda: f.buy(cliente,self.cb.get(),float(valores_acoes[i]), quantidade= 100))
        comprar_button.place(x=500, y=90)

        vender_button = tk.Button(self, text="Comprar", command= lambda: f.sell(cliente,self.cb.get(),float(valores_acoes[i]), quantidade= 100))
        vender_button.place(x=550, y=90)
        

#        cb.bind('',f.geradordeserie)
        
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

        #escolhendo a empresa (ainda precisa virar uma def para generalizar)

        with open('{0}.txt'.format(cb.get()),'r') as arquivo:
            valorescsv = arquivo.read()
        linhas= valorescsv.split('\n')
        for linha in linhas:
            x,y= linha.split(',')
            tempo.append(float(x))
            valores_acoes.append(float(y))
            
        progresso= ttk.Progressbar(self, orient=tk.HORIZONTAL, length=500, mode="determinate", maximum=1E6, value= cliente.saldo)
        progresso.place(x=0,y=50)
        
        
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


'''DIFICULDADE MÉDIA'''
class modo_médio(tk.Frame): #dificuldade na qual cada ponto é plotado eixos cada 15 segundos, sendo este o
                            #tempo para tomar eixos decisão de compra ou venda
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        photo = tk.PhotoImage(file='cash.png')
        BGlabel = tk.Label(self, image=photo)
        BGlabel.image = photo
        BGlabel.place(x=0, y=0)
        
        cb= ttk.Combobox(values=('AAPL', 'ACN', 'ADBE', 'AVGO', 'BIDU', 'BTI', 'BUD', 'CHL', 'CL', 'CRM', 'CSCO', 'DEO', 'ECL', 'EL', 'F', 'FB', 'GM', 'GOOG (1)', 'GOOGL (1)', 'HMC', 'IBM', 'INTC', 'KO', 'MDLZ', 'MO', 'MSFT (2)', 'MU', 'NKE', 'NVDA', 'ORCL', 'PEP', 'PHG', 'PM', 'QCOM', 'SAP', 'SNE', 'STZ', 'T', 'TM', 'TMUS', 'TSLA', 'TSM', 'TXN', 'UL', 'UN', 'VMW', 'VZ'))
        cb.place(x=0,y=0)
        cb.set('ACN')
    
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Gráficos", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        voltar = tk.Button(self, text="Voltar",command=lambda: controller.show_frame(Difficulty))
        voltar.pack()
        
        comprar_button = tk.Button(self, text="Comprar", command= lambda: f.buy(cliente,cb.get(),valores_acoes[i], quantidade= 100))
        comprar_button.place(x=500, y=90)

        vender_button = tk.Button(self, text="Vender", command= lambda: f.sell(cliente,cb.get,valores_acoes[i], quantidade= 100))
        vender_button.place(x=550, y=90)
        
#        fig = Figure(figsize=(5,4), dpi=100)
#        self.eixos = fig.add_subplot(111)
#        self.canvas = FigureCanvasTkAgg(fig, self)
#        self.widget = self.canvas.get_tk_widget()
#        self.eixos.set_autoscale_on(True)
#        self.eixos.set_xlabel('Tempo (dias)')
#        self.eixos.set_ylabel('Valor da ação (dólares)')
#        self.canvas.show()
#        self.canvas.get_tk_widget().pack(side=tk.BOTTOM)
#        self.canvas._tkcanvas.pack(side=tk.LEFT)
#
#        with open('{0}.txt'.format(cb.get()),'r') as arquivo:
#            valorescsv = arquivo.read()
#        linhas= valorescsv.split('\n')
#        for linha in linhas:
#            x,y= linha.split(',')
#            tempo.append(float(x))
#            valores_acoes.append(float(y))
#        time = tk.IntVar()
#        time.set(0)
#        self.timer()       
#    k=0    
#    def timer(self):
#        global k
#        if k < 1260:
#            new_time = time.get() + 1
#            time.set(new_time)
#            
#            self.eixos.set_xlabel('Tempo (dias)')
#            self.eixos.set_ylabel('Valor da ação (dólares)')
#    
#            valor_em_x = tempo[k]
#            valor_em_y = valores_acoes[k]
#            
#            #por extenso e com diametro do ponto
#            self.eixos.plot(valor_em_x, valor_em_y, color='r', marker='o', markersize=3)
#            
#            plt.draw()
#            self.canvas.show()        
##           print para testar iteração sobre a lista
#            print('Valor da ação: U${0} \nDia: {1}'.format(valor_em_y, valor_em_x))
#    
#            label_alteravel= tk.Label(self, text= 'O preço da ação hoje é: U$ {0}'.format(valor_em_y),font=LARGE_FONT)
#            label_alteravel.place(x=0,y=80)
#            
#            money_cliente= tk.Label(self, text= 'Seu saldo atual é de: {0}'.format(cliente.saldo))
#            money_cliente.place(x=0,y=600)
#            
#            root.after(100, self.timer) # call this function again in 1,000 milliseconds
#            k += 1
'''DIFICULDADE ALTA'''     
class modo_difícil(tk.Frame):#dificuldade na qual cada ponto é plotado eixos cada 5 segundos, sendo este o
                             #tempo para tomar eixos decisão de compra ou venda
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        photo = tk.PhotoImage(file='cash.png')
        BGlabel = tk.Label(self, image=photo)
        BGlabel.image = photo
        BGlabel.place(x=0, y=0)
        
        cb= ttk.Combobox(values=('AAPL', 'ACN', 'ADBE', 'AVGO', 'BIDU', 'BTI', 'BUD', 'CHL', 'CL', 'CRM', 'CSCO', 'DEO', 'ECL', 'EL', 'F', 'FB', 'GM', 'GOOG (1)', 'GOOGL (1)', 'HMC', 'IBM', 'INTC', 'KO', 'MDLZ', 'MO', 'MSFT (2)', 'MU', 'NKE', 'NVDA', 'ORCL', 'PEP', 'PHG', 'PM', 'QCOM', 'SAP', 'SNE', 'STZ', 'T', 'TM', 'TMUS', 'TSLA', 'TSM', 'TXN', 'UL', 'UN', 'VMW', 'VZ'))
        cb.place(x=0,y=0)
        cb.set('ACN')
        
        label = tk.Label(self, text="Gráficos", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        voltar = tk.Button(self, text="Voltar",command=lambda: controller.show_frame(Difficulty))
        voltar.pack()

        comprar_button = tk.Button(self, text="Comprar", command= lambda: f.buy(cliente,'tesla',valores_acoes[i], quantidade= 100))
        comprar_button.place(x=500, y=90)

        vender_button = tk.Button(self, text="Vender", command= lambda: f.sell(cliente,'tesla',valores_acoes[i], quantidade= 100))
        vender_button.place(x=550, y=90)

#carteiras={'carteiras':{'cliente':{'carteira':cliente.carteira, 'saldo':cliente.saldo}}}
#firebase.patch('https://projeto-final-dessoft.firebaseio.com/', carteiras)

"""CONFIGURAÇÕES APP [/]"""

#Dimensionar e gerar Loop do jogo
app = jogo()
app.geometry("1220x720")
app.mainloop()



"""FIM CONFIGURAÇÕES APP [/]"""
