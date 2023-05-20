import random
cont = 10   # contador
nd = ''  # nove digitos
for i in range(9):
    nd += str(random.randint(0, 9))
rs = 0  # resultado
for digit in nd:    
    rs += int(digit) * cont
    cont -= 1
digit1 = (rs * 10) % 11

digit1 = digit1 if digit1 <= 9 else 0
print(digit1)

dd = nd + str(digit1)  # dd = dez digitos
cont2 = 11

rs2 = 0  # rs2 = resultado 2
for digit in dd:
    rs2 += int(digit) * cont2
    cont2 -=1  # contador 2
digit2 = (rs2 * 10) % 11

digit2 = digit2 if digit2 <= 9 else 0
print(digit2)


ncpf = f'{nd}{digit1}{digit2}' # ncpf = novo cpf
print(ncpf)