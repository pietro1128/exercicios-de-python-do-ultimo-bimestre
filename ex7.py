num= [0,0,0,0,0,0,0,0,0,0]

for i in range(0,9):
    num[i]= int(input("digite um numero:  "))
    
num_vetor = list(set(num))

print(num_vetor)