def divide(a,b):
    return a % b == 0

print(divide(10,3))
print(divide(195,13))

'''
ricerca binaria cubo
'''

cube=10
start=0
high=cube
epsilon=0.01

middle=(start + high) / 2
while abs((middle**3) - cube) > epsilon:
    if middle**3  < cube: start = middle
    else : high= middle
    middle= (start + high) / 2 

print(middle) 

'''
trasformare numero decimale in binario
'''

num=-1057
string=''
flag=False
if num < 0:
     num= abs(num)
     flag= True

while num > 0:
    if num == 0 : string='0'
    string += str(num%2)
    num= num // 2
if flag: string= '-' + string
print(string)

'''
trasformazione numero decimale in binario
nella memoria vengono salvati due numeri in coppia  (125 , -2) prima si trasforma 125 in base 2 
quindi 1111101 e sarebbero le cifre più importanti invece l'altro numero sarebbe in base due 
e dice dove posizionare la virgola 11111.01 
125 * 2**-2 = 31.25 quindi 11111.01 nella memoria è la rappresentazione di 31.25
'''

x = 31.25
p = 0
# trovare p
while ((2**p) * x) % 1 != 0:
    p += 1
#convertire in binario
num = int(x * (2**p))
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num % 2) + result
    num = num // 2
# aggiungere 0
for i in range(p - len(result)):
    result = '0' + result
# Compone la stringa binaria frazionaria
result = result[:-p] + '.' + result[-p:]

print(f'{p} è il numero corretto')
print('{} rappresentazione binario {}'.format(x, result))



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