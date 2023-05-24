def ler_arquivo(nome_arquivo="input.txt"):
    with open(nome_arquivo) as arquivo:
        numeros = arquivo.readline().split()
        dicionario = {
            "quantidade_sistemas": int(numeros[0]),
            "dimensao": int(numeros[1]),
            "precisao": float(numeros[2])
        }
        lista_sistemas = []
        lista_sistemas_b = []
        for _ in range(dicionario["quantidade_sistemas"]):
            sistema = []
            for _ in range(dicionario["dimensao"]):
                linha = list(map(float, arquivo.readline().split()))
                sistema.append(linha)
            lista_sistemas.append(sistema)
            linha_b = list(map(float, arquivo.readline().split()))
            lista_sistemas_b.append(linha_b)
    return dicionario, lista_sistemas, lista_sistemas_b


def gauss_jacobi(dicionario, lista_sistemas, lista_sistemas_b):
    n = range(dicionario['dimensao'])
    lista_resultados = []
    idx = 0
    for a in lista_sistemas:
        lista_b = lista_sistemas_b[idx]
        condicao_de_parada = True

        x = []
        # cálculo do vetor G
        g = []
        for aux in n:
            g.append(lista_b[aux] / a[aux][aux])  # termo independente (diagonal principal) pelo pivô (B)
        print('g:', g)
        iteracao = 1
        while condicao_de_parada:
            if iteracao == 1:
                x = x_anterior = g  # problema no código aqui!!! é definido que na primeira iteração o x = x_anterior = g... (linha 54)
            else:
                x_anterior = x
            print('iteração:', iteracao)
            # gerando a matriz para o cálculo iterativo
            for i in n:
                soma_com_variaveis = 0
                for j in n:
                    if i == j:
                        continue
                    soma_com_variaveis += (-(a[i][j] * x[j]))
                x[i] = (lista_b[i] - soma_com_variaveis) / a[i][i]


            # avaliando critério de parada
            resultado = [abs(x - y) for x, y in zip(x, x_anterior)]  # ... assim, quando chegamos aqui ainda na primeira iteração, os valores sao subtraidos, ou seja, um valor x - x, ou seja, 0 (linha 62)

            print('x:', x)
            print('x_anterior:', x_anterior)

            d = max(resultado)
            dr = d / max(x)

            if dr < dicionario['precisao']:  #  por fim, o valor de dr será 0, assim, sendo menor que o valor da precisao, parando o while com apenas uma iteração
                print('dr:', repr(dr))
                condicao_de_parada = False
                lista_resultados.append(x)

            iteracao = iteracao + 1

        idx += 1

    return lista_resultados


def main():
    r = gauss_jacobi(*ler_arquivo())
    print(r)


if __name__ == "__main__":
    main()
