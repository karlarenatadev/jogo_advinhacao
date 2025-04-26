import random

print("*******************************")
print("Bem vindo ao jogo de Advinhação")
print("*******************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 0

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina um nível: "))

if( nivel == 1 ):
    total_de_tentativas = 20
elif( nivel == 2 ):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range (1, total_de_tentativas + 1) :
    print(f"Tentativa {rodada} de {total_de_tentativas}")
    chute = int(input("Digite um número entre 1 e 100: "))

    print("Você digitou " , chute)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if ( acertou ):
        print("Você acertou!")
        break
    else:
        if( maior ):
            print("Você errou! O seu chute foi maior que o número secreto")
        elif( menor ):
            print("Você errou! O seu chute foi menor que o número secreto")

    rodada = rodada + 1

print("Fim de jogo!")
