#ADICIONAR ESSA PARTE AS FUNCOES UNIVERSAIS[1]

def instrucoes_popup():
    popup =tk.Tk()
    popup.wm_title("Instruções")
    with open('Instrucoes.txt', 'r') as qpt3:
        dificuldade = qpt3.read()
    instrucao_label = tk.Label(popup, text=dificuldade)
    instrucao_label.pack()
    popup.mainloop()
   
#ADICIONAR ESSA PARTE ENTRE container.grid_columnconfigure(0, weight=1) E self.frames = {}\

menu = tk.Menu(container)
        tk.Tk.config(self, menu=menu)

        subMenu = tk.Menu(menu)
        menu.add_cascade(label='Jogo', menu=subMenu)
        subMenu.add_command(label="Salvar Jogo", command=doNothing)
        subMenu.add_command(label="Carreegar Jogo", command=doNothing)

        instrucoesMenu = tk.Menu(menu)
        menu.add_cascade(label='Instruções', menu=instrucoesMenu)
        instrucoesMenu.add_command(label="Guia para Iniciantes", command=instrucoes_popup)
