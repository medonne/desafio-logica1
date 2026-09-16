# Desafio de Projeto 03 - Escrevendo as classes de um Jogo
# Por: Médonne Penteado


# Cria a classe Heroi.
class Heroi:

    def __init__(self, nome, idade, tipo):

        self.nome = nome

        self.idade = idade

        self.tipo = tipo


    def atacar(self):

        # Estrutura de decisão para definir o ataque do herói.

        if self.tipo == "mago":
            ataque = "magia"

        elif self.tipo == "guerreiro":
            ataque = "espada"

        elif self.tipo == "monge":
            ataque = "artes marciais"

        elif self.tipo == "ninja":
            ataque = "shuriken"

        # Caso seja digitado um tipo diferente dos disponíveis.
        else:
            ataque = "ataque desconhecido"

        # Exibe o tipo do herói e o ataque utilizado.
        print(f"O {self.tipo} atacou usando {ataque}")


# Variável utilizada para controlar o laço de repetição.
continuar = "sim"


while continuar == "sim":

    nome = input("Digite o nome do herói: ")

    idade = int(input("Digite a idade do herói: "))

    tipo = input(
        "Digite o tipo do herói (mago, guerreiro, monge ou ninja): "
    ).lower()


    # Cria um objeto chamado heroi utilizando a classe Heroi.
    heroi = Heroi(nome, idade, tipo)


    # Chama o método atacar() do objeto criado.
    heroi.atacar()


    # Pergunta se o usuário deseja criar outro herói.
    # Se responder "sim", o while começa novamente.
    # Se responder outra coisa, o laço termina.
    continuar = input(
        "\nDeseja criar outro herói? (sim/não): "
    ).lower()


# Esta mensagem aparece depois que o while termina.
print("\nPrograma encerrado!")