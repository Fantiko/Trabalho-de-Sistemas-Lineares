import time


def OperacaoPivo(sistema, matrizL, size, k):
    for i in range(k + 1, size):
        matrizL[i][k] = sistema[i][k] / sistema[k][k]  # Calcula o elemento pivô para a linha i
        for j in range(k, size):
            sistema[i][j] -= matrizL[i][k] * sistema[k][j]  # Atualiza os elementos abaixo do pivô


def MatrizL(matrizL, size):
    for i in range(size):
        matrizL[i][i] = 1.0  # Define os elementos diagonais de L como 1
        for j in range(i + 1, size):
            matrizL[i][j] = 0.0  # Define o restante dos elementos de L como 0


def MatrizU(sistema, matrizU, size):
    for i in range(size):
        for j in range(i, size):
            matrizU[i][j] = sistema[i][j]  # Copia os elementos do sistema original para U


def LY(matrizL, arrayR, arrayY, size):
    for i in range(size):
        arrayY[i] = arrayR[i]  # Copia os elementos do vetor do lado direito para Y
        for j in range(i):
            arrayY[i] -= matrizL[i][j] * arrayY[j]  # Realiza a substituição progressiva


def UX(matrizU, arrayY, arrayX, size):
    for i in range(size - 1, -1, -1):
        soma = 0.0
        for j in range(i + 1, size):
            soma += matrizU[i][j] * arrayX[j]  # Calcula a soma dos valores conhecidos de X
        arrayX[i] = (arrayY[i] - soma) / matrizU[i][i]  # Calcula o valor de X


def metodo_lu(dicionario, principal_sistema, lista_sistemas_b):
    lista_resultados = []

    # Leitura da quantidade de matrizes, tamanho do vetor e precisão

    num_matrices = dicionario["quantidade_sistemas"]
    size = dicionario["dimensao"]
    matrizA = principal_sistema

    tempos = []
    for matriz in range(num_matrices):
        inicio = time.perf_counter()

        sistema = [row.copy() for row in matrizA]
        matrizL = [[0.0] * size for _ in range(size)]
        matrizU = [[0.0] * size for _ in range(size)]

        arrayY = [0.0] * size
        arrayX = [0.0] * size

        arrayR = lista_sistemas_b[matriz]

        for k in range(size - 1):
            OperacaoPivo(sistema, matrizL, size, k)

        MatrizL(matrizL, size)
        MatrizU(sistema, matrizU, size)
        LY(matrizL, arrayR, arrayY, size)

        UX(matrizU, arrayY, arrayX, size)
        lista_resultados.append(arrayX)

        fim = time.perf_counter()  # calcular o tempo
        tempo_decorrido = fim - inicio  # calcular o tempo
        tempos.append(tempo_decorrido)  # calcular o tempo

    return lista_resultados, tempos
