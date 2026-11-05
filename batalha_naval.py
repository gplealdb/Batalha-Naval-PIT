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
