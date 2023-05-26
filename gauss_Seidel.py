def ler_arquivo(nome_arquivo="input.txt"):
    with open(nome_arquivo) as arquivo:
        # Lendo a primeira linha do arquivo e convertendo os números em uma lista
        numeros = arquivo.readline().split()
        # Criando um dicionário com as informações lidas do arquivo
        dicionario = {
            "quantidade_sistemas": int(numeros[0]),
            "dimensao": int(numeros[1]),
            "precisao": float(numeros[2])
        }
        # Inicializando listas vazias para armazenar os sistemas e os termos independentes
        sistema = []
        lista_sistemas_b = []

        for _ in range(dicionario["dimensao"]):
            linha = list(map(float, arquivo.readline().split()))
            sistema.append(linha)

        for _ in range(dicionario["quantidade_sistemas"]):
            # Lendo a linha de termos independentes e convertendo os números em uma lista
            linha_b = list(map(float, arquivo.readline().split()))
            # Adicionando os termos independentes à lista de termos independentes
            lista_sistemas_b.append(linha_b)
    # Retornando as informações lidas do arquivo

    print(sistema, lista_sistemas_b)
    return dicionario, sistema, lista_sistemas_b


def warning():
    return 'Não foi possível resolver este sistema com o método Gauss-Jacobi por causa de um zero na diagonal principal.'


def gauss_jacobi(dicionario, principal_sistema, lista_sistemas_b):

    # Gerando uma lista de índices para iteração
    n = range(dicionario['dimensao'])
    # Inicializando uma lista vazia para armazenar os resultados
    lista_resultados = []
    idx = 0
    # Iterando sobre cada sistema

    flag = False
    lista_b = lista_sistemas_b[idx]
    condicao_de_parada = True

    # Inicializando o vetor resposta como uma lista de zeros
    x_resposta = [0] * dicionario['dimensao']
    # Calculando o vetor G
    g = []
    for aux in n:
        # Tratando a divisão por zero
        try:
            g.append(lista_b[aux] / principal_sistema[aux][aux])
        except ZeroDivisionError:
            # Se houver uma divisão por zero, adiciona uma mensagem de erro aos resultados e interrompe o cálculo
            lista_resultados.append([warning()])
            flag = True
            break

    iteracao = 1
    if flag:
        condicao_de_parada = False

    # Loop para realizar as iterações do método de Gauss-Jacobi
    while condicao_de_parada:
        if iteracao == 1:
            x = g
        else:
            x = x_resposta
            x_resposta = [0] * dicionario['dimensao']

        # Calculando os novos valores de x
        last_x = 0
        var_x = []
        for i in n:
            soma_com_variaveis = 0
            for j in n:
                print(j)
                if i == j:
                    continue
                if j > last_x:
                    soma_com_variaveis = soma_com_variaveis + ((-1 * principal_sistema[i][j]) * var_x[j])
                else:
                    soma_com_variaveis = soma_com_variaveis + ((-1 * principal_sistema[i][j]) * x[j])
                var_x[j] = x[j]
                last_x = last_x + 1

            # Tratando a divisão por zero
            x_resposta[i] = (lista_b[i] + soma_com_variaveis) / principal_sistema[i][i]

        # Avaliando a condição de parada
        resultado = [abs(x - y) for x, y in zip(x_resposta, x)]

        d = max(resultado)
        dr = d / max(x_resposta)

        if dr < dicionario['precisao']:
            # Se a condição de parada for satisfeita, adiciona o vetor resposta aos resultados
            condicao_de_parada = False
            lista_resultados.append(x_resposta)

        iteracao = iteracao + 1

        idx += 1

    # Retornando a lista de resultados
    return lista_resultados


def main():
    # Chamando as funções para realizar os cálculos e exibir os resultados
    r = gauss_jacobi(*ler_arquivo())
    print(r)


if __name__ == "__main__":
    main()
