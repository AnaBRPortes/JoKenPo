import random

jogador_vence = 0
adversario_vence = 0

opcoes = ["pedra", "papel", "tesoura"]

while True:
    jogador = input("Pedra, papel ou tesoura? ou use S para sair: ").lower()
    
    if jogador == "s":
        break

    if jogador not in opcoes:
        continue

    numero = random.randint(0, 2)
    adversario_escolha = opcoes[numero]
    print("Adversário escolheu ", adversario_escolha + ".")

    if jogador == adversario_escolha:
        print("Empate!")
    elif (jogador == "pedra" and adversario_escolha == "tesoura") or \
         (jogador == "tesoura" and adversario_escolha == "papel") or \
         (jogador == "papel" and adversario_escolha == "pedra"):
        print("Você ganhou!")
        jogador_vence += 1 
    else:
        print("Você perdeu!")
        adversario_vence += 1

    print("Jogador:", jogador_vence)
    print("Adversário:", adversario_vence)

    print("-------------------------------------------------")

