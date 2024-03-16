from random import choice

escolhas = ["pedra", "papel", "tesoura"]
escolha_jogador = int
escolha_computador = int
score_jogador = 0
score_computador = 0

while escolha_jogador != 0:
    escolha_computador = choice(escolhas)
    escolha_jogador = int(input("""[1] Pedra\n[2] Papel\n[3] Tesoura\n[0] Sair>> Insira a sua escolha: """))

    if escolha_jogador == 0:
        print("Até mais, volte mais vezes para nos divertirmos juntos!")
        break
    elif escolha_jogador < 0:
        print("Por favor, selecione uma opção válida.")
    elif escolha_jogador == 1 and escolha_computador == "tesoura":
        score_jogador += 1
        print(f"Você escolheu {escolhas[escolha_jogador-1]}.")
        print(f"Computador escolheu {escolha_computador}.")
        print(f"Parabéns! Seu score é de:{score_jogador} pontos\n", "=" * 40)
    elif escolha_jogador == 2 and escolha_computador == "pedra":
        score_jogador += 1
        print(f"Você escolheu {escolhas[escolha_jogador-1]}.")
        print(f"Computador escolheu {escolha_computador}.")
        print(f"Parabéns! Seu score é de:{score_jogador} pontos\n", "=" * 40)
    elif escolha_jogador == 3 and escolha_computador == "papel":
        score_jogador += 1
        print(f"Você escolheu {escolhas[escolha_jogador-1]}.")
        print(f"Computador escolheu {escolha_computador}.")
        print(f"Parabéns! Seu score é de:{score_jogador} pontos\n", "=" * 40)
    elif escolhas[escolha_jogador-1] == escolha_computador:
        print(f"Você escolheu {escolhas[escolha_jogador-1]}.")
        print(f"Computador escolheu {escolha_computador}.")
        print(f"Opa... parece que tivemos um empate! Seu score é de:{score_jogador} pontos\n", "=" * 40)
    else:
        score_computador += 1
        print(f"Você escolheu {escolhas[escolha_jogador-1]}.")
        print(f"Computador escolheu {escolha_computador}.")
        print(f"Não foi dessa vez.\nSeu score é de:{score_jogador} pontos\n", "=" * 40)
