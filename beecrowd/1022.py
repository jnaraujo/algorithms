qnt_entradas = int(input(""))

def mmc(a, b):
        while b != 0:
            resto = a % b

            a = b
            b = resto
        return a

for i in range(qnt_entradas):
    entrada = input().split(" ")

    sinal = entrada[3]

    n1, d1, n2, d2 = [float(a) for a in entrada if a not in "/+-*"]


    divisor = 0
    quociente = 0

    divisor2 = 0
    quociente2 = 0


    if sinal == "+":
        divisor = (n1 * d2) + (n2 * d1)
        quociente = d1 * d2
    elif sinal == "-":
        divisor = (n1 * d2) - (n2 * d1)
        quociente = d1 * d2
    elif sinal == "*":
        divisor = n1 * n2
        quociente = d1 * d2
    elif sinal == "/":
        divisor = n1 * d2
        quociente = d1 * n2

    mmc_dq = mmc(divisor, quociente)

    divisor2 = divisor / mmc_dq
    quociente2 = quociente / mmc_dq


    print("{:.0f}/{:.0f} = {:.0f}/{:.0f}".format(divisor, quociente, divisor2, quociente2))