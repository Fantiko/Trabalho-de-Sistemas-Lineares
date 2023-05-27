
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


def limpar_arquivo():
    with open('output.txt', 'w') as arquivo:
        arquivo.write('')


def escrever_arquivo(lista_resultados, lista_tempos,funçao_nome):
    with open("output.txt", "a") as arquivo:
        arquivo.write("_______________")
        for matriz in lista_resultados:
            arquivo.write(f"\n|- Metodo de {funçao_nome}\n| {matriz}\n|- Resolvida em {lista_tempos[lista_resultados.index(matriz)]} segundos.\n|\n|")
        arquivo.write("_______________")

