anno = int(input('Introduzca un año: '))
if anno % 4 == 0 and anno % 100 == 0 and anno % 400 == 0:
    print('El anio es Biciesto')
else:
    print('El anio no es Biciesto')