'''
trasformare numero decimale in binario
'''

num=1057
string=''
while num>0:
    if num == 0 : string='0'
    string += str(num%2)
    num= num // 2

print(string)

'''
floating point error
'''
i=0
for x in range(11):
    i+=0.1
print(i , 0,1*10)
print(i == 1)


questionn=input('put verb: ')
print(f'i can {questionn} better then you')
print((questionn + ' ') * 5)

import math

'''
algoritmo per indovinare la radice quadrata, all'inizio dovrai fornire il numero che pensi sia la radice quadrata di X
se il numero non lo è allora si dovra utilizzare come guess l'output che si ha ottenuto fino a quando non diventa il numero che si avvicina piu possibile 
alla radice quadrata si X
'''

def radice():
    x=int(input('radice quadrata di: '))
    return x

def guess():
    g=input('guess: ')
    return g

X=radice()
R= math.sqrt(X)

def calcolo():
    G=guess()
    G=float(G)
    nextGuess= G - ((G**2) - X) / (2*G**2)
    print(nextGuess)
    if nextGuess != R: calcolo()
    else: return nextGuess

calcolo()

'''
potenza
'''
G=0
x=int(input('Number: '))
while G**2 < x:
    G+=1
if G**2==x: print(f'{G} è il quadrato di {x}')
elif x<0:print(f'intendevi {-x} ?')
else:print(f'{x} non è un quadrato perfetto')