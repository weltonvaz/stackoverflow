while True:
    tamanho = int(input())
    if tamanho in range(1, 25):
        tabela = []
        for x in range(0, tamanho):
            tabela.append(["O"]*tamanho)
        for y in tabela:
            print("".join(y))
            '''tabela[(len(tabela)+1)/2] = "X"
            posicao_do_x = len(tabela)/2
            posicao_do_x2 = int(posicao_do_x) // int(y)
            posicao_do_x3 = int(posicao_do_x) % int(y)
            tabela[int(posicao_do_x2)][int(posicao_do_x3)] = "X"'''
        print("@")
    else:
        break
