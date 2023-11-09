lista = [6,3,1,8,7,4,3,2,3,4,5,3,1]
pares = []
for e in lista:
    if e%2==0:
        pares.append(e)
    else:
        continue

print(f'Os pares são: {pares}')
