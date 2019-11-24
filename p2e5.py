cantbilletes1000 = 9
cantbilletes500 = 19
cantbilletes100 = 99 

papeletas1k = 0
papeletas500 = 0
papeletas100 = 0

disponnible = (cantbilletes1000 * 1000) + (cantbilletes500 * 500) + (cantbilletes100 * 100)
print(disponnible)

def menu():
    print('''##########Bienvenido al Cajero Automatico#######
    ######### Opcion 1 - Banco ABC ##########################
    ######### Opcion 2 - Banco Banninter ####################''')
print(menu())
print()
while (True):
    opcion = int(input('Introduzca la opcion deseada: ')) 
    if (opcion == 1):
        limiteRetiro = 10000
        print('Bienvenido al Banco ABC')
        retiro = int(input('Ingrese una Cantidad deseada a retirar: '))
        if retiro > limiteRetiro:
            print('El monto solocitado excede el limite por transacion')
        elif retiro % 100 != 0 or retiro > disponnible:
            print('El monto solicitado no puede ser dispensado')
        else:
            #while retiro > 0:
            # Retiro de 1000 
            if retiro > 1000:
                papeletas1k = retiro // 1000
                retiro = retiro - (papeletas1k * 1000)
                print(f'Billetes de mil {papeletas1k}')
            # Retiro de 500
            if retiro > 500:
                papeletas500 = retiro // 500
                retiro = retiro - (papeletas500 * 500)
                print(f'Billetes de quinientos {papeletas500} ')
            # Retiro de 100
            if retiro > 100:
                papeletas100 = retiro // 100
                retiro = retiro - (papeletas100 * 100)
                print(f'Billetes de cien {papeletas100}') 
            elif retiro == 0:
                print("Sera enviado al menu principal")

    
    elif opcion == 2:
        print('Banco Baninter')
        retiro2 = int(input('Ingrese el monto a retirar: '))
        limiteRetiro = 2000
        if retiro2 > limiteRetiro:
            print('El monto no puede ser dispensado')
        elif retiro2 % 100 != 0 or retiro2 > disponnible:
            print('El monto solicitado no puede ser dispensado')
        
        else:
            #while retiro > 0:
            # Retiro de 1000 
            if retiro2 > 1000:
                papeletas1k = retiro2 // 1000
                retiro = retiro2 - (papeletas1k * 1000)
                print(f'Billetes de mil {papeletas1k}')
            # Retiro de 500
            if retiro2 > 500:
                papeletas500 = retiro2 // 500
                retiro2 = retiro2 - (papeletas500 * 500)
                print(f'Billetes de quinientos {papeletas500} ')
            # Retiro de 100
            if retiro2 > 100:
                papeletas100 = retiro2 // 100
                retiro2 = retiro2 - (papeletas100 * 100)
                print(f'Billetes de cien {papeletas100}') 
            elif retiro2 == 0:
                print("Sera enviado al menu principal")


    elif opcion == 3:
        print('Gracias por usar el Cajero')
        break   
    
    else:
        print('Se ha equivocado de opcion; Elija una correcta')
