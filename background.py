#ADICIONAR O CODIGO A SEGUIR NO INCIO DE TODA PAGINA EM QUE QUEIRA ADICIONAR O BACKGROUND, DEPOIS DE tk.Frame.__init__(self, parent) 
#PARA ESCOLHER O BACKGROUND DA LABEL EX:tk.Label(self, text='blablabla',bg = 'cor')
#PARA ESCOLHER A COR DO TEXTO DA LABEL EX:tk.Label(self, text='blablabla', fg='cor')

photo = tk.PhotoImage(file='cash.png')
        BGlabel = tk.Label(self, image=photo)
        BGlabel.image = photo
        BGlabel.place(x=0, y=0)
