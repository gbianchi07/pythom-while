cont = 1 
contapar= 0

while cont <= 10:
    numero = int(input('informe um numero:'))
    if numero % 2 ==0:
        contapar += 1
    cont +=1

print(f'quantidade de par:{contapar}')


