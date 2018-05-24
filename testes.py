class listabox:
  def __init__(self):
    self.escolhido='TSLA'
    
    
    for item in ['AAPL', 'ACN', 'ADBE', 'AVGO', 'BIDU', 'BTI', 'BUD', 'CHL', 'CL', 'CRM', 'CSCO', 'DEO', 'ECL', 'EL', 'F', 'FB', 'GM', 'GOOG (1)', 'GOOGL (1)', 'HMC', 'IBM', 'INTC', 'KO', 'MDLZ', 'MO', 'MSFT (2)', 'MU', 'NKE', 'NVDA', 'ORCL', 'PEP', 'PHG', 'PM', 'QCOM', 'SAP', 'SNE', 'STZ', 'T', 'TM', 'TMUS', 'TSLA', 'TSM', 'TXN', 'UL', 'UN', 'VMW', 'VZ']:
            listbox.insert(END, item)
            
  def CurSelect(self,event):
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(selection[0])
    self.escolhido= picked
    print(escolhido)

listbox=Listbox(root)
listbox.bind('<<ListboxSelect>>',CurSelect)
listbox.place(x=0,y=90)
root.mainloop()
