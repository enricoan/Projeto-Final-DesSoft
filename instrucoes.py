#incorparar ao codigo principal

class Instructions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        with open('Instrucoes.txt', 'r') as qpt3:
            dificuldade = qpt3.read()
        instrucao_label = tk.Label(self, text=dificuldade)
        instrucao_label.pack()
