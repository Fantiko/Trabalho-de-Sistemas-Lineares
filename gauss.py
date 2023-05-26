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
    return dicionario, sistema, lista_sistemas_b


def warning():
    return 'Não foi possível resolver este sistema'


def eliminacao_gauss(dicionario, sistema, lista_sistemas_b):
    for matriz in lista_sistemas_b:  # fazer todos os sitemas
        flag = False
        for etapa in range(dicionario["dimensao"]):  # para cada linha do sistema
            pivo = sistema[etapa][etapa]  # o pivo é o Akk da matriz
            if pivo == 0:  # 0 na diagonal principal
                for i in range(etapa + 1, dicionario["dimensao"]):
                    if sistema[i][etapa] != 0:
                        sistema[etapa], sistema[i] = sistema[i], sistema[etapa]
                        pivo = sistema[etapa][etapa]
                        break
                else:
                    flag = True
                    continue
            if flag:
                lista_sistemas_b[lista_sistemas.index(sistema)] = warning()
                break

            sistema[etapa] = [elemento / pivo for elemento in sistema[etapa]]
            matriz[etapa] = matriz[etapa] / pivo
            for i in range(dicionario["dimensao"]):
                if i != etapa:
                    fator = sistema[i][etapa]
                    sistema[i] = [elemento - fator * sistema[etapa][j] for j, elemento in enumerate(sistema[i])]
                    matriz[i] = \
                        matriz[i] - fator * \
                        matriz[etapa]

    return lista_sistemas_b


def main():
    print(ler_arquivo())
    print(eliminacao_gauss(*ler_arquivo()))


if __name__ == "__main__":
    main()
