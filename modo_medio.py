# -*- coding: utf-8 -*-
"""
Created on Thu May 24 08:43:53 2018

@author: Enrico Aloisi Nardi
"""
'''DIFICULDADE MÉDIA'''


import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.pyplot as plt

m=0 #contador do tempo
class modo_medio(tk.Frame): #dificuldade na qual cada ponto é plotado eixos cada 15 segundos, sendo este o
                            #tempo para tomar a decisão de compra ou venda
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        photo = tk.PhotoImage(file='cash.png')
        BGlabel = tk.Label(self, image=photo)
        BGlabel.image = photo
        BGlabel.place(x=0, y=0)

        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Gráficos", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        voltar = tk.Button(self, text="Voltar",command=lambda: controller.show_frame(Difficulty))
        voltar.pack()
        
        botao_comprar = tk.Button(self, text="Vender", command= lambda: f.buy(cliente,'AAPL',valores_acoes[i], quantidade= 100))
        botao_comprar.place(x=500, y=90)

        botao_vender = tk.Button(self, text="Comprar", command= lambda: f.sell(cliente,'AAPL',valores_acoes[i], quantidade= 100))
        botao_vender.place(x=550, y=90)
        
        listbox = tk.Listbox(self)
        listbox.place(x=0,y=0)
        for item in ['AAPL', 'ACN', 'ADBE', 'AVGO', 'BIDU', 'BTI', 'BUD', 'CHL', 'CL', 'CRM', 'CSCO', 'DEO', 'ECL', 'EL', 'F', 'FB', 'GM', 'GOOG (1)', 'GOOGL (1)', 'HMC', 'IBM', 'INTC', 'KO', 'MDLZ', 'MO', 'MSFT (2)', 'MU', 'NKE', 'NVDA', 'ORCL', 'PEP', 'PHG', 'PM', 'QCOM', 'SAP', 'SNE', 'STZ', 'T', 'TM', 'TMUS', 'TSLA', 'TSM', 'TXN', 'UL', 'UN', 'VMW', 'VZ']:
            listbox.insert(END, item)
        
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
        
        #linha que chama a função gerador de serie presente em outro arquivo python. esta função le os arquivos txt
        # e produz as series que serão plotadas
        tempo,valores_acoes= f.geradordeserie('TSLA')

    
    def timer_medio(self):
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
#           print para testar iteração sobre a lista
            print('Valor da ação: U${0} \nDia: {1}'.format(valor_em_y, valor_em_x))
    
            label_alteravel= tk.Label(self, text= 'O preço da ação hoje é: U$ {0}'.format(valor_em_y),font=LARGE_FONT)
            label_alteravel.place(x=0,y=80)
            
            money_cliente= tk.Label(self, text= 'Seu saldo atual é de: {0}'.format(cliente.saldo))
            money_cliente.place(x=0,y=600)
            
            self.after(100, self.timer) # call this function again in 1,000 milliseconds
            print(k)
            m += 1
            
            self.timer() 