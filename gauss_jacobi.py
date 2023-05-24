def ler_arquivo(nome_arquivo="input.txt"):
    with open(nome_arquivo) as arquivo:
        numeros = arquivo.readline().split()
        dicionario = {
            "quantidade_sistemas": int(numeros[0]),
            "dimensao": int(numeros[1]),
            "precisao": float(numeros[2])
        }
        lista_sistemas = []
        sistema = []
        lista_sistemas_b = []
        for sistemas in range(dicionario["quantidade_sistemas"]):
            for iterador in range(dicionario["dimensao"]):
                linha = list(map(float, arquivo.readline().split()))
                sistema.append(linha)
            lista_sistemas.append(sistema)
            linha_b = list(map(float, arquivo.readline().split()))
            lista_sistemas_b.append(linha_b)
    return dicionario, lista_sistemas, lista_sistemas_b


def gauss_jacobi(dicionario, lista_sistemas, lista_sistemas_b):
    n = range(dicionario['dimensao'])
    lista_resultados = []

    for a in lista_sistemas:
        condicao_de_parada = True
        x = []

        # calulo do vetor G
        g = []
        for aux in n:
            g.append(float(lista_sistemas_b[aux]) / a[aux][aux])  # termo independente(diagonal principal) pelo pivô(B)

        iteracao = 1
        while condicao_de_parada:

            if iteracao == 1:
                x, x_anterior = g
            else:
                x_anterior = x

            for i in n:
                soma_com_variaveis = 0
                for j in n:
                    if i == j:
                        continue
                    soma_com_variaveis += (-1 * (a[i][j] * x[j]))
                x[i] = (lista_sistemas_b[i] - soma_com_variaveis) / a[i][i]

            # avaliando critério de parada

            iteracao += 1


def main():
    gauss_jacobi(*ler_arquivo())


if __name__ == "__main__":
    main()
