import os
def transformador(f, path):
    if f[:-3] == 'csv':
        no_ext = f.strip('.csv')
        with open('{0}/{1}'.format(path, f), 'r') as entrada:
            linhas = entrada.readlines()
        saida_lista=[]
        for i in range(1, len(linhas)):
            linha = linhas[i]
            dados = linha.split(',')
            saida_lista.append("{0},{1}".format(i-1,dados[5]))
        saida_string = '\n'.join(saida_lista)
        with open('{0}/{1}.txt'.format(path, no_ext),'w') as saida:
            saida.write(saida_string)

path = 'PATH TO CSV FILES THAT U WANT TO CHANGE'
d = os.listdir(path)
print(d)
for f in range(len(d)):
    transformador(d[f], path)