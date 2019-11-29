tabla = input('Tabla: ')
nuemro = input('Hasta que numero: ')

tabla = int(tabla)
nuemro = int(nuemro) + 1

for x in range (1, nuemro):
    print (str(tabla)+'x'+str(x)+'='+str(x*tabla))
