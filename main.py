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


def eliminacao_gauss(dicionario, lista_sistemas, lista_sistemas_b):
    for sistema in lista_sistemas:  # fazer todos os sitemas
        for etapa in range(dicionario["dimensao"]):  # para cada linha do sistema
            pivo = sistema[etapa][etapa]  # o pivo é o Akk da matriz

            if pivo == 0:  # 0 na diagonal principal
                for i in range(etapa + 1, dicionario["dimensao"]):
                    if sistema[i][etapa] != 0:
                        sistema[etapa], sistema[i] = sistema[i], sistema[etapa]
                        pivo = sistema[etapa][etapa]
                        break
                else:
                    continue

            sistema[etapa] = [elemento/pivo for elemento in sistema[etapa]]
            lista_sistemas_b[lista_sistemas.index(sistema)][etapa] = lista_sistemas_b[lista_sistemas.index(sistema)][etapa]/pivo

            for i in range(dicionario["dimensao"]):
                if i != etapa:
                    fator = sistema[i][etapa]
                    sistema[i] = [elemento - fator * sistema[etapa][j] for j, elemento in enumerate(sistema[i])]
    return lista_sistemas_b


def main():
    print(eliminacao_gauss(*ler_arquivo()))
    

if __name__ == "__main__":
    main()
