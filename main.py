import sys

from gauss import *
from gauss_jacobi import *
from gauss_seidel import *
from lu import *
from utilidade import *


def main(nome_arquivo="input.txt"):
    # lista com as funções em sequência
    funcoes = [eliminacao_gauss, gauss_jacobi, gauss_seidel, metodo_lu]
    limpar_arquivo()
    for funcao in funcoes:
        lista_resultados, lista_tempos = funcao(*ler_arquivo(nome_arquivo))
        escrever_arquivo(lista_resultados, lista_tempos, funcao.__name__)


if __name__ == "__main__":
    main()
    if len(sys.argv) != 2:
        print("faltou o nome do arquivo")
        sys.exit(1)

    # Obtém o argumento fornecido
    argumento = sys.argv[1]
    # Chama a função main com o argumento
    main(argumento)
