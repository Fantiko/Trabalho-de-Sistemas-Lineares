def lerarquivo(nomearquivo="input.txt"):
    with open(nomearquivo) as arquivo:
        numeros = arquivo.readline().split()
        dicionario = {
            "quantidade_sistemas": int(numeros[0]),
            "dimensao": int(numeros[1]),
            "precisao": float(numeros[2])
        }
        
def main():
    lerarquivo()


if __name__ == "__main__":
    main()
