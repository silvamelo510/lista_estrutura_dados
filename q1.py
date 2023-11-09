elemento = input('')
lista = [6,3,1,8,7,4,3,2,3,4,5,3,1]
contador= 0
for e in lista:
    if e == int(elemento):
        contador+= 1
    elif(e == elemento):
        contador+=1
    else:
        continue
print(contador)