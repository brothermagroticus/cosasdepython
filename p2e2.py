def menu():
    print("""Bienvenido al convertidor 300
    ##### OPCION 1 ######
    # Convertidor C* a F* #
    ##### OPCION 2 ######
    # Conversor de Divisas: Dolar a Peso #
    ##### OPCION 3 ######
    # Conversor de Metros a Pies # 
    ##### Para Salir Ingrese ingrese el #4 """)
    #continuar = 0 = False
    #salir = 4 = True

while(True):
    opcion = int(input('Introduce una opcion deseada: '))
    if (opcion == 1):
        print('Bienvenido al conversor de C* a F*')
        celsius = input("Introduzca grados Celsius: ")
        celsius = int(celsius)
        fahrenheit = (celsius * 1.8) + 32
        print("La temperatura es: ", fahrenheit,"F*")
    
    elif (opcion == 2):
        def dolares():
            pesos = float(input('Ingrese la cantidad en dolares a convertir: '))
            return pesos * 53.18
        print("Esta es la cantidad en Pesos: ", dolares())
        
    elif (opcion == 3):
        def pies():
            metros = float(input("Introduzca cantidad en Metros: "))
            return metros * 3.28
        print('Son ', pies(), "pies")
        
    elif (opcion == 4):
        print('Gracias por usar el Conversor 300')
        break

    elif (opcion == 1,2,3,4):
        print('Por favor, ingrese una opcion Valida')