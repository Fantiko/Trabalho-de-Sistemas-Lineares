
# ler arquivo que lê apenas a matriz principal e pega todos valores de b
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
        lista_sistemas = []
        lista_sistemas_b = []
        # Iterando sobre a quantidade de sistemas especificada no arquivo
        for _ in range(dicionario["quantidade_sistemas"]):
            # Lendo as linhas do sistema e convertendo os números em uma matriz
            sistema = []
            for _ in range(dicionario["dimensao"]):
                linha = list(map(float, arquivo.readline().split()))
                sistema.append(linha)
            # Adicionando o sistema à lista de sistemas
            lista_sistemas.append(sistema)
            # Lendo a linha de termos independentes e convertendo os números em uma lista
            linha_b = list(map(float, arquivo.readline().split()))
            # Adicionando os termos independentes à lista de termos independentes
            lista_sistemas_b.append(linha_b)
    # Retornando as informações lidas do arquivo
    return dicionario, lista_sistemas, lista_sistemas_b

def main():
    print(ler_arquivo())

if __name__ == "__main__":
    main()
