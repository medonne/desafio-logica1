# Desafio de Projeto 01 - Lógica de Programação
# Por: Médonne Penteado

continuar = "sim"

# Laço de repetição
while continuar == "sim":

    # Variáveis
    heroi = input("Digite o nome do herói: ")
    xp = int(input("Digite a quantidade de XP: "))

    # Estrutura de decisão
    if xp <= 1000:
        nivel = "Ferro"

    elif xp <= 2000:
        nivel = "Bronze"

    elif xp <= 5000:
        nivel = "Prata"

    elif xp <= 7000:
        nivel = "Ouro"

    elif xp <= 8000:
        nivel = "Platina"

    elif xp <= 9000:
        nivel = "Ascendente"

    elif xp <= 10000:
        nivel = "Imortal"

    else:
        nivel = "Radiante"

    # Saída
    print(f"O Herói de nome {heroi} está no nível de {nivel}")

    # Pergunta se deseja repetir
    continuar = input("Deseja cadastrar outro herói? sim/não: ")