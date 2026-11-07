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


def jogar_partida(jogadores, placar, historico):
    """jogadores = ((nome1, navios1), (nome2, navios2))."""
    tabuleiros = [criar_tabuleiro(TAMANHO), criar_tabuleiro(TAMANHO)]
    tiros = [set(), set()]
    turno = 0
    vencedor = ""

    while vencedor == "":
        nome = jogadores[turno][0]
        navios = jogadores[turno][1]
        print("\nVez de:", nome)
        mostrar_tabuleiro(tabuleiros[turno])

        linha = ler_numero("Linha (1 a 5): ", 1, 5) - 1
        coluna = ler_numero("Coluna (1 a 5): ", 1, 5) - 1
        posicao = (linha, coluna)

        if posicao in tiros[turno]:
            print("Você já atirou aí. Escolha outra posição.")
        else:
            tiros[turno].add(posicao)
            if posicao in navios:
                tabuleiros[turno][linha][coluna] = "X"
                print("Acertou!")
            else:
                tabuleiros[turno][linha][coluna] = "O"
                print("Água!")

            if contar_acertos(navios, tiros[turno]) == len(navios):
                vencedor = nome
            else:
                turno = 1 - turno

    print("\n*** VITÓRIA DE", vencedor, "***")
    placar[vencedor] = placar[vencedor] + 1
    historico.append(vencedor)
    print("Placar:", placar)

def mostrar_estatisticas(historico, placar):
    """Desafio escolhido: estatísticas da sessão - Parte 1."""
    total = len(historico)
    print("\nESTATÍSTICAS DA SESSÃO")
    print("Total de partidas:", total)
    for nome in placar:
        vitorias = historico.count(nome)
        porcentagem = 0
        if total > 0:
            porcentagem = vitorias * 100 / total
        print(nome + ":", vitorias, "vitória(s) -", round(porcentagem, 1), "%")

    maior = 0
    atual = 0
    anterior = ""
    for vencedor in historico:
        if vencedor == anterior:
            atual = atual + 1
        else:
            atual = 1
            anterior = vencedor
        if atual > maior:
            maior = atual
    print("Maior sequência de vitórias seguidas:", maior)

def main():
    print("=== BATALHA NAVAL SIMPLIFICADA ===")
    nome1 = input("Nome do jogador 1: ").strip()
    nome2 = input("Nome do jogador 2: ").strip()
    if nome1 == "":
        nome1 = "Jogador 1"
    if nome2 == "" or nome2 == nome1:
        nome2 = "Jogador 2"

    jogadores = ((nome1, NAVIOS_J1), (nome2, NAVIOS_J2))
    placar = {nome1: 0, nome2: 0}
    historico = []
