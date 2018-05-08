""""BIBLIOTECA [*]"""

#bibliotecas matplotlib
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style

#Bibliotecas tkinter
import tkinter as tk
from tkinter import ttk

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

        for F in (MenuPage, Game, Credits, PageThree, ScoreBoard):

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
        one = tk.Label(self, text="Million Run")

        one.place(x=1280 / 2, y=0)

        carteira = tk.Label(self, text="Carteira", font=LARGE_FONT)

        carteira.place(x=1100, y=100)

        obtidos_texto = "Microsoft,\n Sony,\n LG"
        obtidos = tk.Label(self, text=obtidos_texto, font=NORMAL_FONT)

        obtidos.place(x=1100, y=150)

        Selecione = tk.Label(self, text="Selecione a ação que deseja alterar", font=LARGE_FONT)
        Selecione.place(x=50, y=100)
        botao_comprar = tk.Button(self, text="Buy",
                               command=buy)
        botao_comprar.place(x=400, y=450)

        botao_vender = tk.Button(self, text="Sell",
                              command=sell)
        botao_vender.place(x=400, y=500)

        grafico = tk.Label(self, text="Grafico")
        grafico.place(x=200, y=475)

        total = tk.Label(self, text="Total: X REAIS", font=NORMAL_FONT)
        total.place(x=1100, y=650)

""""FIM JOGO [4]"""


""""CRÉDITOS [5]"""

class Credits(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        titulo = tk.Label(self, text="Créditos", font=LARGE_FONT)
        titulo.pack(pady=10,padx=10)

        texto_creditos = "Henrico:blablabla\nGuilherme:Blablabla\nJadson:blablabla"
        creditos = tk.Label(self, text=texto_creditos, font=NORMAL_FONT)
        creditos.pack()
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MenuPage))

        button1.pack()

""""FIM CRÉDITOS [5]"""


""""PÁGINA GRÁFICO [6] // TESTE"""
class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(MenuPage))
        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

""""PÁGINA GRÁFICO [6] // TESTE"""


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