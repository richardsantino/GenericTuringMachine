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

## -- execução da maquina de turing -- #
if len(simbolos) <= 30 and int(n_estados) <= 50: # verifica se a maquina tem configurações que ultrapassam o limite.
    for fita in palavras:
        if len(fita) <= 100: # verifica se a fita esta no limite de caracteres.
            turing_machine.run(fita, n_estados, transicoes)
        else: 
            print(fita, "não executada, pois ultrapassa o limite de 100 caracteres")
else:
    print("configurações de entrada invalidas, revise e entrada de texto e tente novamente.")