qnt_jogadas = int(input())

def play(a, b):
    if a == "tesoura" and b == "papel":
        return 0
    elif a == "papel" and b == "pedra":
        return 0
    elif a == "pedra" and b == "lagarto":
        return 0
    elif a == "lagarto" and b == "Spock":
        return 0
    elif a == "Spock" and b == "tesoura":
        return 0
    elif a == "tesoura" and b == "lagarto":
        return 0
    elif a == "lagarto" and b == "papel":
        return 0
    elif a == "papel" and b == "Spock":
        return 0
    elif a == "Spock" and b == "pedra":
        return 0
    elif a == "pedra" and b == "tesoura":
        return 0
    elif a == b:
        return -1
    else:
        return 1
    
for i in range(qnt_jogadas):
    Sheldon, Raj = input().split(" ")


    winner = play(Sheldon, Raj)

    if winner == 0:
        print(f"Caso #{i+1}: Bazinga!")
    elif winner == 1:
        print(f"Caso #{i+1}: Raj trapaceou!")
    else:
        print(f"Caso #{i+1}: De novo!")