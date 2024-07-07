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
radice quadrata
'''
G=0
x=int(input('Number: '))
while G**2 <= x:
    if G**2==x: print(f'{G} è il quadrato di {x}')
    else:print(f'{G} non è la potenza di {x}')
    G+=1