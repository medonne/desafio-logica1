# Desafio de Projeto 02 - Calculadora de Partidas Rankeadas
# Por: Médonne Penteado


# Função para calcular o saldo de vitórias e o nível do jogador
def calcular_rank(vitorias, derrotas):

    saldo = vitorias - derrotas

    # Estrutura de decisão para definir o nível
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

    # Retorna o saldo de vitórias e o nível
    return saldo, nivel


# Variável para controlar a repetição
continuar = "sim"


# Laço de repetição
while continuar == "sim":

    # Entrada de dados
    vitorias = int(input("Digite a quantidade de vitórias: "))
    derrotas = int(input("Digite a quantidade de derrotas: "))

    # Chama a função e guarda os resultados
    saldoVitorias, nivel = calcular_rank(vitorias, derrotas)

    # Exibe o resultado
    print(f"O Herói tem saldo de {saldoVitorias} e está no nível de {nivel}")

    # Pergunta se o usuário deseja fazer outro cálculo
    continuar = input("Deseja calcular outro jogador? (sim/não): ").lower()

if continuar == "não" or continuar == "nao":
    print("Obrigado por jogar! Até a próxima!")