def calcular_rank(vitorias, derrotas):
    saldo = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nivel = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo, nivel


continuar = "sim"

while continuar == "sim":
    vitorias = int(input("Digite a quantidade de vitórias: "))
    derrotas = int(input("Digite a quantidade de derrotas: "))

    saldoVitorias, nivel = calcular_rank(vitorias, derrotas)

    print(f"O Herói tem saldo de {saldoVitorias} e está no nível de {nivel}")

    continuar = input("Deseja calcular outro jogador? (sim/não): ")