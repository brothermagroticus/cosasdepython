def menu():
    print("""Bienvenido al Calculador 300
    ##### OPCION 1 ######
    # Calcular Impuesto sobre la Renta #
    ##### OPCION 2 ######
    # Calcular Seguro Familiar de Salud #
    ##### OPCION 3 ######
    # Calcualr Administradora de Fondo de Pensiones  # 
    ##### Para Salir Ingrese ingrese el #4 """)
    #continuar = 0 = False
    #salir = 4 = True
print(menu())
while(True):
    opcion = int(input('Introduce una opcion deseada: '))
    if (opcion == 1):
        def impuestossobrerenta():
            print('Favor de ingresar su sueldo Neto mensual: ')
## El impuesto se cobra dependiendo de el sueldo Neto del individuo
## Si es mas de 34684 el porcentaje sera de 0.20
## Si es mas de 79776 el porcentaje sera de 0.25
        while (True):
            sueldo = float(input('Ingrese su sueldo neto: '))
            if (sueldo == 0):
                print('Sera enviado al menu Principal')
                break

            elif (sueldo <= 34683.33):
                print('Usted no aplica para el cobro de ISR')

            elif (sueldo >= 34683.34):
                sueldo = sueldo *0.20
                print(sueldo)

            elif (sueldo >= 52027.41):
                sueldo = sueldo*0.20
                print('El monto a pagar es: ', sueldo)

            elif (sueldo >= 79776.01):
                sueldo = sueldo*0.25
                print('El monto a pagar es: ', sueldo)
       
    
    elif (opcion == 2):
        while (True):
            def sueldoneto():
                impuestoars = float(input('Ingese su sueldo Neto Mensual: '))
                return impuestoars * 0.0304
            print('El cobro del AFP es de: ', sueldoneto())
            
            if (sueldoneto() == 0):
                print('Sera enviado al menu principal')
                break    
            

        
    elif (opcion == 3):
        while (True):
            def sueldoneto2():
                impuestoafp = float(input('Ingese su sueldo Neto Mensual: '))
                return impuestoafp * 0.0287
            print('El cobro del AFP es de: ', sueldoneto())
            if (sueldoneto2() == 0):
                print('Usted sera enviado el menu Principal')
                break
        
        
    elif (opcion == 4):
        print('Gracias por usar el Calculador 300')
        break

    elif (opcion == 1,2,3,4):
        print('Por favor, ingrese una opcion Valida')