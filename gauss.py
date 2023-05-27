import time
from utilidade import *


def warning():
    return 'Não foi possível resolver este sistema'


def eliminacao_gauss(dicionario, sistema, lista_sistemas_b):
    tempos = []  # calcular o tempo
    for matriz in lista_sistemas_b:  # fazer todos os sitemas
        inicio = time.perf_counter()  # calcular o tempo

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

            sistema[etapa] = [elemento / pivo for elemento in sistema[etapa]]
            matriz[etapa] = matriz[etapa] / pivo
            for i in range(dicionario["dimensao"]):
                if i != etapa:
                    fator = sistema[i][etapa]
                    sistema[i] = [elemento - fator * sistema[etapa][j] for j, elemento in enumerate(sistema[i])]
                    matriz[i] = matriz[i] - fator * matriz[etapa]

        fim = time.perf_counter()  # calcular o tempo
        tempo_decorrido = fim - inicio  # calcular o tempo
        tempos.append(tempo_decorrido)  # calcular o tempo

    return lista_sistemas_b, tempos
