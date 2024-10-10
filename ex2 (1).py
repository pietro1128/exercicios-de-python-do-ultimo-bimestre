num= [0,0,0,0,0,0,0,0,0,0]
maior=-1
menor=999
for i in range(0,9):
    num[i]= int(input("digite um numero:  "))
    if num[i] < menor:
        menor = num[i]
    elif num[i] > maior:
        maior = num[i]
print("o maior numero é ",maior, "\n")
print("e o menor numero é ",menor)