from tkinter import *
import tkinter as tk
def doNothing():
    print('nothing')
def close():
    tk.destroy()

root = Tk()

menu = tk.Menu(root)
root.config(menu=menu)

subMenu = tk.Menu(menu)
menu.add_cascade(label='Jogo', menu=subMenu)
subMenu.add_command(label="Salvar Jogo", command=doNothing)
subMenu.add_command(label="Carreegar Jogo", command=doNothing)

instrucoesMenu = tk.Menu(menu)
menu.add_cascade(label='Instruções', menu=instrucoesMenu)
instrucoesMenu.add_command(label="Guia para Iniciantes", command=doNothing)



tk.mainloop()