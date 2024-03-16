from winsound import Beep
from time import sleep

alfabeto_morse = {
    "a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.", "0":"-----"
}

print("Bem vindo ao Tradutor de Texto para Morse!")
texto = str(input("Insira a palavra/texto que você deseja traduzir/ouvir em código morse: "))
salvar = int
codigo_morse = ''

for i in texto.lower():
    if i.lower() in alfabeto_morse.keys():
        for simbolo in alfabeto_morse[i]:
            if simbolo == ".":
                Beep(500, 500)
                sleep(0.2)
            elif simbolo == "-":
                Beep(700, 1000)
                sleep(0.2)
            codigo_morse += simbolo
    elif i == " ":
        codigo_morse += "/"
    else:
        codigo_morse += "(?)"
        sleep(1.3)

print(codigo_morse)

while True:
    salvar = int(input("Você deseja salvar o código em um arquivo de texto?\n[0] Sim\n[1] Não\n>> Insira sua opção: "))

    if salvar == 0:
        nome_arq = str(input("Por favor, dê um nome ao seu arquivo: "))
        arquivo = open("Código Morse\\" + nome_arq + ".txt", "w")
        arquivo.write(f"Texto:\n{texto.lower()}\nTraduzido Morse:\n{codigo_morse}")
        arquivo.close()
        print(f'O seu arquivo "{nome_arq}" foi salvo com sucesso!')
        print("Obrigado por usar nosso serviço, até mais!")
        quit()
    elif salvar == 1:
        print("Obrigado por usar nosso serviço, até mais!")
        quit()
    else:
        print("Por favor, digite uma opção válida.")
        continue