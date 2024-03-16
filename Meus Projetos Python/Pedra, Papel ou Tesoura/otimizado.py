from random import choice

escolhas = ["pedra", "papel", "tesoura"]
combs_possiveis = {
    "pedra":{
        "pedra":"empate", "papel":"perde", "tesoura":"ganha"
    },
    "papel":{
        "pedra":"ganha", "papel":"empata", "tesoura":"perde"
    },
    "tesoura":{
        "pedra":"perde", "papel":"ganha", "tesoura":"empate"
    }
}

score_jogador = 0

while True:
    escolha_computador = choice(escolhas)
    escolha_jogador = int(input("[1] Pedra\n[2] Papel\n[3] Tesoura\n[0] Sair\n>> Insira a sua escolha: "))

    if escolha_jogador == 0:
        print("Foi um prazer, volte mais vezes para nos divertirmos juntos!")
        break
    elif escolha_jogador not in [1, 2, 3]:
        print("Por favor, digite uma opção válida.")
        continue

    # Aqui pode ficar um pouco complexo de se interpretar, então vamos lá...
    # - A variável resultado irá receber o dicionário onde mapeei todas as condições e o caminho do valor que dará o resultado da combinação.
    # - Irá considerar o valor descrito pelo jogador.
    # - Como o dicionário não possui o index, tento buscar chamando pelo nome do item escolhido pelo usuário na lista escolhas e assim consigo acessar a Key do meu dicionário de maneira simples.
    # - Por fim, a escolha_computador vai acessar o valor da chave (outro dicionário) e acessar a chave desse novo dicionário, obtendo o valor do resultado.
    
    resultado = combs_possiveis[escolhas[escolha_jogador-1]][escolha_computador]
    if resultado == "ganha":
        score_jogador += 1
        print(f"Parabéns, seu score atual é {score_jogador} pontos.\n", "=" * 40)
    elif resultado == "empate":
        print(f"Opa... parece que tivemos um empate! Seu score é de: {score_jogador} pontos\n", "=" * 40)
    else:
        print(f"Não foi dessa vez. Seu score é de: {score_jogador} pontos\n", "=" * 40)