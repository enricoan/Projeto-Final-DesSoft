""""BIBLIOTECAS"""
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
import time

#importar o key_press_handler
from matplotlib.backend_bases import key_press_handler

""""FIM BIBLIOTECAS [*]"""
cliente=Cliente()
carteira_cliente= broker.mostracarteira(cliente)

""""FONTES PADRÃO E STYLE [0]"""
LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
style.use("ggplot")
""""FIM FONTES PADRÃO E STYLE [0]"""

#função que carrega o texto das instruções do jogo e as exibe num pop-up quando chamada
def instrucoes_popup():
    popup =tk.Tk()
    popup.wm_title("Instruções")
    with open('txts/' + 'Instrucoes.txt', 'r') as qpt3:
        dificuldade = qpt3.read()
    instrucao_label = tk.Label(popup, text=dificuldade)
    instrucao_label.pack()
    popup.mainloop()

#página inicial do jogo: abre uma label grande com todas as instruções e botões 
#com os nomes das dificuldades
class TelaInicial(object):
    def __init__(self, parent):
#        super(TelaInicial, self).__init__(parent)
        self.controller = parent
        self.iniciarView()
        self.nome = "TELA_INICIAL"
        
        self.viewFacil      = modo_facil(self)
        self.viewFacil.geometry("1500x720")
        self.viewFacil.withdraw()

        self.viewMedio      = modo_medio(self)
        self.viewMedio.geometry("1500x720")
        self.viewMedio.withdraw()
         
        self.viewDificil    = modo_dificil(self)
        self.viewDificil.geometry("1500x720")
        self.viewDificil.withdraw()
        
        self.viewPersonalizado = modo_personalizado(self)
        self.viewPersonalizado.geometry("1500x720")
        self.viewPersonalizado.withdraw()
        
        self.viewCurrent = None
        self.currentName = None
        
    def hide(self):
        self.controller.withdraw()

    def show(self):
        self.controller.update()
        self.controller.deiconify()
        
        
    def iniciarView(self):
        label_dificuldade = tk.Label(self.controller, text="Escolha a dificuldade", font=LARGE_FONT)
        label_dificuldade.place(x=0,y=0)
        
        button_dif1 = tk.Button(self.controller, text="Fácil", command=lambda:self.setCurrentView("FACIL"), font=NORMAL_FONT)
        button_dif1.pack(fill=tk.BOTH)
        
        button_dif2 = tk.Button(self.controller, text="Real", command=lambda:self.setCurrentView("MEDIO"), font=NORMAL_FONT)
        button_dif2.pack(fill=tk.BOTH)
        
#        button_dif3 = tk.Button(self.controller, text="Real",   command=lambda:self.setCurrentView("DIFICIL"), font=NORMAL_FONT)
#        button_dif3.pack(fill=tk.BOTH)
#
#        button_dif4 = tk.Button(self.controller, text="Personalizado",   command=lambda:self.setCurrentView("PERSONALIZADO"), font=NORMAL_FONT)
#        button_dif4.pack(fill=tk.BOTH)
        
        with open('txts/' + 'Instrucoes.txt', 'r') as qpt3:
            dificuldade = qpt3.read()
        instrucao_label = tk.Label(self.controller, text=dificuldade)
        instrucao_label.pack() 
        
    def setCurrentView(self, newViewName):
        newViewName = newViewName.upper()

        if self.currentName == newViewName:
            return;

        if self.currentName == "MEDIO" or self.currentName == "DIFICIL":
            self.viewCurrent.timer_stop() 

        if self.viewCurrent is not None:
            self.viewCurrent.hide()
            self.viewCurrent.reset()
            self.currentName = None
                        
        self.currentName = newViewName
       
        if "FACIL" == newViewName:
            self.viewCurrent    = self.viewFacil
        elif "MEDIO" == newViewName:
            self.viewCurrent = self.viewMedio
        elif "DIFICIL" == newViewName:
            self.viewCurrent = self.viewDificil
        elif "PERSONALIZADO" == newViewName:
            self.viewCurrent = self.viewPersonalizado
        else:
            return

        self.viewCurrent.show()
"""FIM DIFICULDADE"""

'''FACIL'''
class modo_facil(tk.Toplevel): #modo do jogo no qual eixos pessoa clica no botão e o valor da ação é plotado
    def __init__(self, parent, manual = True):
        super(modo_facil, self).__init__()
        
        photo = tk.PhotoImage(file='cash.png')
        BGlabel = tk.Label(self, image=photo)
        BGlabel.image = photo
        BGlabel.place(x=0, y=0)
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
        self.selecionada='AAPL'
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
                                command= lambda: broker.buy(cliente,self.selecionada,\
                                float(self.valores_acoes[self.idx]), self.linkedValue, quantidade= 100))
        botao_comprar.place(x=500, y=90)

        botao_vender = tk.Button(self, text="Vender", \
                                 command= lambda: broker.sell(cliente,self.selecionada,float \
                                (self.valores_acoes[self.idx]), self.linkedValue, quantidade= 100))
        botao_vender.place(x=580, y=90)
        

        progresso= ttk.Progressbar(self, orient=tk.HORIZONTAL, length=670, mode="determinate", maximum=1E6, variable = self.linkedValue)
        progresso.place(x=400,y=600)
        
        label_empresa= tk.Label(self, text= 'Escolha a empresa na qual quer investir', font= LARGE_FONT)
        label_empresa.place(x=0,y=0)
        
        

        
        #lista com as empresas que podem ser escolhidas pelo usuário
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listboxEmpresas = tk.Listbox(self, yscrollcommand=self.scrollbar.set)
        self.listboxEmpresas.bind('<<ListboxSelect>>', self.CurSelect)
        
        self.listboxEmpresas.place(x=4,y=20)
        self.list = ['AAPL', 'ACN', 'ACIEL','ADBE', 'AVGO', 'BIDU', 'BTI', 'BUD', 'CHL','CIENDADOS', 'CL','CODESIGN',\
                     'CRM', 'CSCO', 'DEO', 'ECL', 'EL', 'F','FABLAB', 'FB','GDE', 'GM', 'GOOG (1)', \
                     'GOOGL (1)', 'HMC', 'IBM','INSPER','ISNTRUMED', 'INTC', 'KO','MATVAR', 'MDLZ', 'MO','MODSIM', 'MSFT (2)', \
                     'MU','NATDES', 'NKE', 'NVDA', 'ORCL', 'PEP', 'PHG', 'PM', 'QCOM', 'SAP', \
                     'SNE', 'SOFTDES', 'STZ', 'T', 'TM', 'TMUS', 'TSLA', 'TSM', 'TXN', 'UL', 'UN', 'VMW', 'VZ']
        
        for item in self.list:
            self.listboxEmpresas.insert(tk.END, item)
            
        #tudo o que precisamos para o gráfico atualizável
        fig = Figure(figsize=(10,4), dpi=100)
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
        self.listboxEmpresas.unbind('<<ListboxSelect>>')
        self.withdraw()

    def show(self):
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
        self.selecionada=picked
        self.idx = 0
        self.carregado = True

    def proximo_ponto(self):
        if not self.carregado:
            return
        
        if self.idx >= len(self.tempo):
            self.timer_stop()
            return
        
        self.eixos.set_xlabel('Tempo (dias)') 
        self.eixos.set_ylabel('Valor da ação (dólares)')
        
        valor_em_x = self.tempo[self.idx]
        valor_em_y = self.valores_acoes[self.idx]
        
        #por extenso e com diametro do ponto
        self.eixos.plot(valor_em_x, valor_em_y, color='r', marker='o', markersize=3)
        self.canvas.show()
        
        print('Valor da ação: U${0} \nDia: {1}'.format(valor_em_y, valor_em_x))

        label_alteravel= tk.Label(self, text= 'O preço da ação hoje é: U$ {0}'.format(valor_em_y), font=LARGE_FONT)
        label_alteravel.place(x=0,y=500)
        
        money_cliente= tk.Label(self, text= 'Seu saldo atual é de: U$ {0}'.format(cliente.saldo), font=LARGE_FONT)
        money_cliente.place(x=0,y=600)
        
        carteira_label= tk.Label(self, text='Seu carteira possui: Ação | Quantidade \n {0}'.format(broker.mostracarteira(cliente)), font=LARGE_FONT)
        carteira_label.place(x=950, y=200)
        
        lucro_label= tk.Label(self, text='Seu lucro percentual atual é: {0}'.format(broker.mostralucro(cliente, self.idx)), font=LARGE_FONT)
        lucro_label.place(x=0, y=650)
        
        self.idx += 1
'''FIM FACIL'''

'''MEDIO'''
class modo_medio(modo_facil):
    def __init__(self, parent):
        super(modo_medio, self).__init__(parent, False)
        self.currentPeriod = 1000 #local onde o tempo entre a plotagem de um ponto e outro é definida para o modo medio
        
        labelFrame = tk.Frame(self)
        tk.Label(labelFrame, text="Não se esqueça, neste modo você tem 1 segundo\n para decidir se compra ou vende uma ação!").grid(row=0,column=0)
        labelFrame.place(x=800,y=105)

        self.plotTimer = InfiniteTimer(self.currentPeriod, lambda:self.proximo_ponto())
        self.nome = "MEDIO"

    def CurSelect(self, event):
        super(modo_medio, self).CurSelect(event)
        # somente habilita os botoes se houver carregado algum arquivo
        self.plotTimer.start()

    def timer_start(self):
        if not self.carregado:
            return
        if self.currentPeriod != self.period.get():
            self.currentPeriod = self.period.get()
            self.plotTimer.cancel()
            self.plotTimer.destroy()
            self.plotTimer = InfiniteTimer(self.currentPeriod, lambda:self.proximo_ponto())
        self.plotTimer.start()
        
    def timer_stop(self):
        self.plotTimer.cancel()
'''FIM MEDIO'''

'''DIFICIL'''
class modo_dificil(modo_facil):
    def __init__(self, parent):
        super(modo_dificil, self).__init__(parent, False)
        self.currentPeriod = 800 #local onde o tempo entre a plotagem de um ponto e outro é definida para o modo dificil
        
        labelFrame = tk.Frame(self)
        tk.Label(labelFrame, text="Não se esqueça, neste modo você tem 1 segundo\n para decidir se compra ou vende uma ação!").grid(row=0,column=0)
        labelFrame.place(x=800,y=105)

        self.plotTimer = InfiniteTimer(self.currentPeriod, lambda:self.proximo_ponto())
        self.nome = "MEDIO"

    def CurSelect(self, event):
        super(modo_medio, self).CurSelect(event)
        # somente habilita os botoes se houver carregado algum arquivo
        self.plotTimer.start()

    def timer_start(self):
        if not self.carregado:
            return
        if self.currentPeriod != self.period.get():
            self.currentPeriod = self.period.get()
            self.plotTimer.cancel()
            self.plotTimer.destroy()
            self.plotTimer = InfiniteTimer(self.currentPeriod, lambda:self.proximo_ponto())
        self.plotTimer.start()
        
    def timer_stop(self):
        self.plotTimer.cancel()        
        self.nome = "DIFICIL"
'''FIM DIFICIL'''

'''PERSONALIZADO'''
class modo_personalizado(modo_medio):
    def __init__(self,parent):
        super(modo_personalizado, self).__init__(parent)
        
        self.period = IntVar() # tkInter atualiza automaticamente
        self.period.set(15)
        
        self.currentPeriod = self.period.get()
        
        labelFrame = tk.Frame(self)
        tk.Label(labelFrame, text="Período(milisegundos)").grid(row=0, column=0)
        tk.Entry(labelFrame, width=10, textvariable=self.period).grid(row=0, column=2)
        labelFrame.place(x=800,y=105)
        self.nome = "PERSONALIZADO"
        
        #botões da página        
        self.buttonIniciar= tk.Button(self, text="Iniciar", command = lambda:self.timer_start(), state=tk.DISABLED)
        self.buttonIniciar.place(x=1000,y=100)

        self.buttonParar= tk.Button(self, text="Parar", command = lambda:self.timer_stop(), state=tk.DISABLED)
        self.buttonParar.place(x=1000,y=150)
        
    def CurSelect(self, event):
        super(modo_medio, self).CurSelect(event)
        # somente habilita os botoes se houver carregado algum arquivo
        self.buttonIniciar.config(state=tk.NORMAL) 
        self.buttonParar.config(state=tk.NORMAL)
        self.plotTimer.start()
        
    def timer_stop(self):
        self.plotTimer.cancel()
'''PERSONALIZADO'''
        
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
        subMenu.add_command(label="Salvar Jogo", command=  lambda: broker.popupsalvamento(cliente))
        subMenu.add_command(label="Carregar Jogo", command = lambda: broker.popucarregamento(cliente))

        instrucoesMenu = tk.Menu(menu)
        menu.add_cascade(label='Instruções', menu=instrucoesMenu)
        instrucoesMenu.add_command(label="Guia para Iniciantes", command=instrucoes_popup)
     
        self.telaInicial   = TelaInicial(parent)
        self.telaInicial.show()
        
    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.update()
        self.root.deiconify()

"""CONFIGURAÇÕES APP [/]"""

def main():
    root = tk.Tk()
    #root.geometry("1220x720")
    app = Jogo(root)
    root.mainloop()
  
if __name__ == "__main__":
    main()

"""FIM CONFIGURAÇÕES APP [/]"""
