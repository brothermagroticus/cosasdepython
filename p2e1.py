sumaTotal= 0

while (True):
    numero = int(input("Introduce un nuemro: "))
    if (numero == 0):
        print("Usted a salido del bucle")
        break
    sumaTotal = sumaTotal + numero

print(("La suma total es: {} ").format(sumaTotal))