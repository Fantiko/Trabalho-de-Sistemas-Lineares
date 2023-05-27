class Lu:
    def __init__(self, size):
        self.size = size
        self.sistema = np.zeros((size, size))
        self.matrizL = np.zeros((size, size))
        self.matrizU = np.zeros((size, size))
        self.arrayY = np.zeros(size)
        self.arrayR = np.zeros(size)
        self.arrayX = np.zeros(size)

    def ImprimeMatriz(self, matriz):
        for i in range(self.size):
            print()
            for j in range(self.size):
                print(f'{matriz[i][j]:.2f}', end=' ')
        print()

    def ImprimeVetor(self, vetor):
        for i in range(self.size):
            print(f'{vetor[i]:.2f}')
        print()

    def OperacaoPivo(self, k):
        for i in range(k + 1, self.size):
            self.matrizL[i][k] = self.sistema[i][k] / self.sistema[k][k]
            for j in range(k, self.size):
                self.sistema[i][j] -= self.matrizL[i][k] * self.sistema[k][j]

    def MatrizL(self):
        for i in range(self.size):
            self.matrizL[i][i] = 1.0
            for j in range(i + 1, self.size):
                self.matrizL[i][j] = 0.0

    def MatrizU(self):
        for i in range(self.size):
            for j in range(i, self.size):
                self.matrizU[i][j] = self.sistema[i][j]

    def LY(self):
        for i in range(self.size):
            self.arrayY[i] = self.arrayR[i]
            for j in range(i):
                self.arrayY[i] -= self.matrizL[i][j] * self.arrayY[j]

    def UX(self):
        for i in range(self.size - 1, -1, -1):
            sum = 0.0
            for j in range(i + 1, self.size):
                sum += self.matrizU[i][j] * self.arrayX[j]
            self.arrayX[i] = (self.arrayY[i] - sum) / self.matrizU[i][i]


filename = "entrada.txt"

with open(filename, 'r') as file:
    # Leitura da quantidade de matrizes, tamanho do vetor e precisão
    line = file.readline().split()
    num_matrices = int(line[0])
    size = int(line[1])
    matrizA = np.zeros((size, size))

    # Leitura da matriz A
    for i in range(size):
        matrizA[i] = list(map(float, file.readline().split()))

    for _ in range(num_matrices):
        lu = Lu(size)

        # Definir a matriz A para cada iteração
        lu.sistema = matrizA.copy()

        # Leitura da matriz B
        lu.arrayR = list(map(float, file.readline().split()))

        print("\nMatriz A:")
        lu.ImprimeMatriz(lu.sistema)

        for k in range(size - 1):
            lu.OperacaoPivo(k)

        print("\n\nMatriz L:")
        lu.MatrizL()
        lu.ImprimeMatriz(lu.matrizL)

        print("\n\nMatriz U:")
        lu.MatrizU()
        lu.ImprimeMatriz(lu.matrizU)

        print("\n\nVetor Y:")
        lu.LY()
        lu.ImprimeVetor(lu.arrayY)

        print("\n\nVetor X (Solução):")
        lu.UX()
        lu.ImprimeVetor(lu.arrayX)