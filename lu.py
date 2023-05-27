import time

def ImprimeMatriz(matriz, size):
    for i in range(size):
        print()
        for j in range(size):
            print(f'{matriz[i][j]:.2f}', end=' ')
    print()

def ImprimeVetor(vetor, size):
    for i in range(size):
        print(f'{vetor[i]:.2f}')
    print()

def OperacaoPivo(sistema, matrizL, size, k):
    for i in range(k + 1, size):
        matrizL[i][k] = sistema[i][k] / sistema[k][k]
        for j in range(k, size):
            sistema[i][j] -= matrizL[i][k] * sistema[k][j]

def MatrizL(matrizL, size):
    for i in range(size):
        matrizL[i][i] = 1.0
        for j in range(i + 1, size):
            matrizL[i][j] = 0.0

def MatrizU(sistema, matrizU, size):
    for i in range(size):
        for j in range(i, size):
            matrizU[i][j] = sistema[i][j]

def LY(matrizL, arrayR, arrayY, size):
    for i in range(size):
        arrayY[i] = arrayR[i]
        for j in range(i):
            arrayY[i] -= matrizL[i][j] * arrayY[j]

def UX(matrizU, arrayY, arrayX, size):
    for i in range(size - 1, -1, -1):
        sum = 0.0
        for j in range(i + 1, size):
            sum += matrizU[i][j] * arrayX[j]
        arrayX[i] = (arrayY[i] - sum) / matrizU[i][i]


filename = "input.txt"

with open(filename, 'r') as file:
    # Leitura da quantidade de matrizes, tamanho do vetor e precisão
    line = file.readline().split()
    num_matrices = int(line[0])
    size = int(line[1])
    matrizA = [[0.0] * size for _ in range(size)]

    # Leitura da matriz A
    for i in range(size):
        matrizA[i] = list(map(float, file.readline().split()))

    tempos = []
    for _ in range(num_matrices):
        inicio = time.perf_counter()
        sistema = [row.copy() for row in matrizA]
        matrizL = [[0.0] * size for _ in range(size)]
        matrizU = [[0.0] * size for _ in range(size)]
        arrayR = [0.0] * size
        arrayY = [0.0] * size
        arrayX = [0.0] * size

        # Leitura da matriz B
        arrayR = list(map(float, file.readline().split()))

        print("\nMatriz A:")
        ImprimeMatriz(sistema, size)

        for k in range(size - 1):
            OperacaoPivo(sistema, matrizL, size, k)

        print("\n\nMatriz L:")
        MatrizL(matrizL, size)
        ImprimeMatriz(matrizL, size)

        print("\n\nMatriz U:")
        MatrizU(sistema, matrizU, size)
        ImprimeMatriz(matrizU, size)

        print("\n\nVetor Y:")
        LY(matrizL, arrayR, arrayY, size)
        ImprimeVetor(arrayY, size)

        print("\n\nVetor X (Solução):")
        UX(matrizU, arrayY, arrayX, size)
        ImprimeVetor(arrayX, size)
        fim = time.perf_counter()  # calcular o tempo
        tempo_decorrido = fim - inicio  # calcular o tempo
        tempos.append(tempo_decorrido)  # calcular o tempo

    print(tempos)  # calcular o tempo
