from gauss import *
from gauss_jacobi import *
from utilidade import *

def main():
    # lista com as funções em sequência
    funcoes = [eliminacao_gauss]
    limpar_arquivo()
    for funcao in funcoes:

        lista_resultados, lista_tempos = funcao(*ler_arquivo())
        escrever_arquivo(lista_resultados, lista_tempos, funcao.__name__)



if __name__ == "__main__":
    main()
