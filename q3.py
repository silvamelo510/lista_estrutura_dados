maior = 0
menor = 999
lista = [6,3,1,8,7,4,3,2,3,4,5,3,1]
for e in lista:
    if e >= maior:
        maior = e
    if e <= menor:
        menor = e

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')