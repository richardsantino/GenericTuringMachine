class turing_machine:
    def run(entrada, n_estados, transicoes):
        #inicializa as variaveis da maquina
        i_cabecote = 0
        fita = []
        estado_atual = '1'
        estado_aceitacao = n_estados

        #organiza a fita
        for char in entrada:
            fita.append(char)
        fita.append('-')

        while(True):
            #print(fita)
            #print("\nestado atual:", estado_atual, "\nposição cabeçote: ", i_cabecote)
            #print("cabeçote lendo:", fita[i_cabecote])
            #adiciona espaço na lista, pq talvez o cobeçote precise de espaço
            if fita[i_cabecote] == '-': fita.append('-')

            #obtem a regra de transição daquele estado e posição do cabeçote
            transicao = []
            for regra in transicoes:
                if regra[0] == estado_atual and regra[1] == fita[i_cabecote]:
                    transicao = regra
                    break

            #verifica se existe transição e se chegou no estado de aceitação 
            if not transicao and estado_atual == estado_aceitacao: #se não existe transição mas a maquina chegou no estado de aceitação; aceite
                print(entrada, "OK")
                return
            elif not transicao: #se não existe transição; recuse
                print(entrada, "NOT OK")
                return

            #modifica a fita na posição do cabeçote
            fita[i_cabecote] = transicao[2]

            #movimenta o cabeçote
            if transicao[3] == "D": i_cabecote+= 1
            elif transicao[3] == "E": i_cabecote-= 1

            #troca de estado
            estado_atual = transicao[4]