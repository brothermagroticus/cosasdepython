min = 10
max = 456657

cont = 0

print('Los capicuas encontrados son los sigtes: ')
for i in range(min,max+1):
    nums=str(i)
    numl=list(nums)
    if numl == numl[::-1]:
        cap= ''.join(numl)
        cont += 1
        print(cap)
print(f'Total de Capicuas: {cont} ')