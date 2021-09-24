from turing_machine import turing_machine

# lê o arquivo txt de entrada e joga em uma array
f = open("input.txt","r")
file = f.readlines()
f.close()

# remove \n de cada linha do arquivo e joga em um array
entrada_linhas = []
for line in file:
    entrada_linhas.append(line.strip())

## ---- extraindo instruções do txt ---- ##

simbolos = entrada_linhas[0] # simbolos do alfabeto de entrada e do alfabeto da fita concatenados
n_estados = entrada_linhas[1]
n_transicoes = int(entrada_linhas[2])
transicoes = []
n_teste = int(entrada_linhas[n_transicoes+3])
palavras = []

# adiciona as transições em um array
for i in range(3, n_transicoes+3):
    transicao = entrada_linhas[i].split()
    transicoes.append(transicao)

# adiciona as palavras q serão testadas em um array
for i in range(n_transicoes+4, n_transicoes+4+n_teste):
    palavra = entrada_linhas[i]
    palavras.append(palavra)

#print(simbolos, n_estados, n_transicoes)
#print(transicoes)
#print(n_teste, palavras)

for entrada in palavras:
    turing_machine.run(entrada, n_estados, transicoes)

# -- formato do txt --
# linha 1 -> simbolos de entrada com o simbolos da fita.                max de 30 simbolos
# linha 2 -> numero de estados, o ultimo estado é sempre o qaceita.     max de 50 estados
# linha 3 -> as transições
# linha depois das n transições -> um inteiro especificando o numero de palavras que deverão ser testadas pela maquina
# seguida das n palavras em cada linha.                                 max de 100 simbolos por fita