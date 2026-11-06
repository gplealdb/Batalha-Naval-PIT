# BATALHA NAVAL - Trabalho da 3ª Avaliação
# Cada jogador tem o seu tabuleiro e os seus navios (posições diferentes).

TAMANHO = 5
NAVIOS_J1 = {(0, 1), (1, 3), (2, 2), (3, 0), (4, 4)}  # conjunto de tuplas
NAVIOS_J2 = {(0, 4), (1, 0), (2, 3), (3, 2), (4, 1)}

def criar_tabuleiro(tamanho):
    """Recebe o tamanho e devolve uma matriz cheia de '.'."""
    tabuleiro = []
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            linha.append(".")
        tabuleiro.append(linha)
    return tabuleiro


def mostrar_tabuleiro(tabuleiro):
    """Mostra a matriz com os números das linhas e colunas."""
    print("\n    1 2 3 4 5")
    for i in range(len(tabuleiro)):
        print(" " + str(i + 1), end="  ")
        for j in range(len(tabuleiro[i])):
            print(tabuleiro[i][j], end=" ")
        print()

def ler_numero(mensagem, minimo, maximo):
    """Lê um número válido entre minimo e maximo e devolve."""
    while True:
        entrada = input(mensagem).strip()
        if entrada.isdigit():
            numero = int(entrada)
            if numero >= minimo and numero <= maximo:
                return numero
        print("Entrada inválida! Digite de " + str(minimo)
              + " a " + str(maximo) + ".")

def contar_acertos(navios, tiros):
    """Devolve quantos navios já foram atingidos."""
    acertos = 0
    for posicao in navios:
        if posicao in tiros:
            acertos = acertos + 1
    return acertos