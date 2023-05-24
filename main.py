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


def main():
    print(ler_arquivo())


if __name__ == "__main__":
    main()
