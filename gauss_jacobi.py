import time
from utilidade import *

def warning():
    return 'Não foi possível resolver este sistema com o método Gauss-Jacobi por causa de um zero na diagonal principal.'


def gauss_jacobi(dicionario, principal_sistema, lista_sistemas_b):

    # Gerando uma lista de índices para iteração
    n = range(dicionario['dimensao'])
    # Inicializando uma lista vazia para armazenar os resultados
    lista_resultados = []
    idx = 0
    # Iterando sobre cada sistema
    tempos = []  # calcular o tempo

    for b in lista_sistemas_b:
        inicio = time.perf_counter()  # calcular o tempo
        flag = False
        lista_b = b
        condicao_de_parada = True

        # Inicializando o vetor resposta como uma lista de zeros
        x_resposta = [0] * dicionario['dimensao']
        # Calculando o vetor G
        g = []
        for aux in n:
            # Tratando a divisão por zero
            try:
                g.append(lista_b[aux] / principal_sistema[aux][aux])
            except ZeroDivisionError:
                # Se houver uma divisão por zero, adiciona uma mensagem de erro aos resultados e interrompe o cálculo
                lista_resultados.append([warning()])
                flag = True
                break

        iteracao = 1
        if flag:
            condicao_de_parada = False

        # Loop para realizar as iterações do método de Gauss-Jacobi
        while condicao_de_parada:
            if iteracao == 1:
                x = g
            else:
                x = x_resposta
                x_resposta = [0] * dicionario['dimensao']

            # Calculando os novos valores de x
            for i in n:
                soma_com_variaveis = 0
                for j in n:
                    if i == j:
                        continue
                    soma_com_variaveis = soma_com_variaveis + ((-1 * principal_sistema[i][j]) * x[j]) #-1250 -3.75

                # Tratando a divisão por zero
                x_resposta[i] = (lista_b[i] + soma_com_variaveis) / principal_sistema[i][i]

            # Avaliando a condição de parada
            resultado = [abs(x - y) for x, y in zip(x_resposta, x)]
            #  print('resultado: ', resultado)
            #  print('x_resposta: ', x_resposta)
            d = max(resultado)
            dr = d / abs(max(x_resposta))
            #  print('d: ', d)
            #  print('dr: ', dr)
            if dr < dicionario['precisao']:
                # Se a condição de parada for satisfeita, adiciona o vetor resposta aos resultados
                condicao_de_parada = False
                lista_resultados.append(x_resposta)

            iteracao = iteracao + 1
        fim = time.perf_counter()  # calcular o tempo
        tempo_decorrido = fim - inicio  # calcular o tempo
        tempos.append(tempo_decorrido)  # calcular o tempo

            #idx += 1

    # Retornando a lista de resultados
    return lista_resultados , tempos
